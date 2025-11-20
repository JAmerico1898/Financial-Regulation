# app.py
# Explorador Pedagógico dos Acordos de Basileia
# Streamlit App em Português - 100% funcional e didático

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import base64
from datetime import datetime

# ==================== CONFIGURAÇÃO DA PÁGINA ====================
st.set_page_config(
    page_title="Acordos de Basileia - Explorador Pedagógico",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== ESTILOS PERSONALIZADOS ====================
st.markdown("""
<style>
    .big-font {font-size: 50px !important; font-weight: bold; text-align: center; color: #1E90FF;}
    .medium-font {font-size: 28px !important; font-weight: bold;}
    .success-box {padding: 15px; border-radius: 10px; background-color: #d4edda; border: 1px solid #c3e6cb; color: #155724;}
    .warning-box {padding: 15px; border-radius: 10px; background-color: #fff3cd; border: 1px solid #ffeaa7; color: #856404;}
    .danger-box {padding: 15px; border-radius: 10px; background-color: #f8d7da; border: 1px solid #f5c6cb; color: #721c24;}
    .info-box {padding: 15px; border-radius: 10px; background-color: #d1ecf1; border: 1px solid #bee5eb; color: #0c5460;}
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR COM NAVEGAÇÃO ====================
with st.sidebar:
    st.image("https://www.bis.org/img/bislogo_og.jpg", width=200)
    st.title("🏦 Navegação")
    
    modulo = st.radio("Escolha o módulo:",
        ["🏠 Introdução", 
         "1️⃣ Ativos Ponderados por Risco (RWA)", 
         "2️⃣ Simulador de Risco de Crédito", 
         "3️⃣ Alavancagem x Capital Baseado em Risco",
         "4️⃣ Simulação Integrada - Construa seu Banco",
         "🧠 Quiz & Recursos"]
    )
    
# ==================== MÓDULO: INTRODUÇÃO ====================
if modulo == "🏠 Introdução":
    st.markdown('<p class="big-font">Acordos de Basileia</p>', unsafe_allow_html=True)
    st.markdown('<p class="medium-font" style="text-align:center;">Entendendo os Requisitos de Capital Bancário</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1,1])
    with col1:
        st.image("https://www.datocms-assets.com/17507/1606822567-balancopatrimonialestruturaeelementos.png", 
                        caption="Balanço Patrimonial Simplificado", use_container_width=True)    
    with col2:
        st.markdown("""
        ### Por que os bancos precisam de capital?
        
        O capital próprio funciona como um **amortecedor** contra perdas inesperadas.
        
        Em 2008, muitos bancos tinham capital insuficiente para absorver as perdas com hipotecas subprime → **crise financeira global**.
        
        Os **Acordos de Basileia** (I, II, III e IV) foram criados pelo Comitê de Basileia para:
        - Garantir que os bancos tenham capital suficiente
        - Reduzir o risco de falências bancárias
        - Proteger depositantes e a economia
        
        Neste app você vai **aprender fazendo**: construindo portfólios, simulando crises e gerenciando bancos virtuais.
        """)
    
    st.divider()
    st.success("Navegue pelos módulos no menu lateral para começar sua jornada!")

# ==================== MÓDULO 1: RWA PLAYGROUND ====================
elif modulo == "1️⃣ Ativos Ponderados por Risco (RWA)":
    st.header("Módulo 1: Ativos Ponderados por Risco (RWA)")
    st.markdown("### Aprenda como a composição do portfólio afeta o capital exigido")
    
    with st.expander("🎯 Objetivos de aprendizagem"):
        st.write("- Entender pesos de risco de crédito por classe de ativo\n- Ver como o RWA impacta o capital mínimo exigido (8%)\n- Comparar estratégias conservadoras vs. agressivas")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Monte seu portfólio (total = $100 milhões)")
        
        cash = st.slider("Caixa e títulos públicos (0%)", 0, 100, 20)
        gov_bonds = st.slider("Títulos soberanos AAA (0-20%)", 0, 100-cash, 15)
        mortgages = st.slider("Hipotecas residenciais (35-75%)", 0, 100-cash-gov_bonds, 30)
        corp_loans = st.slider("Empréstimos corporativos investment grade (100%)", 0, 100-cash-gov_bonds-mortgages, 20)
        high_yield = st.slider("High-yield / Subinvestment (100-150%)", 0, 100-cash-gov_bonds-mortgages-corp_loans, 10)
        unrated = st.slider("Não classificados (150%)", 0, 100-cash-gov_bonds-mortgages-corp_loans-high_yield, 5)
        
        total_assets = cash + gov_bonds + mortgages + corp_loans + high_yield + unrated
        if total_assets != 100:
            st.warning(f"Total: ${total_assets}M (ajuste para $100M)")
            total_assets = 100
        
        # Pesos médios simplificados (Basel III padronizado)
        rwa = (cash * 0 + gov_bonds * 0.1 + mortgages * 0.5 + corp_loans * 1.0 + high_yield * 1.2 + unrated * 1.5) * 1e6
        required_capital = rwa * 0.08
        car = (12e6 / rwa) * 100 if rwa > 0 else 100  # Supondo capital inicial de $12M
        
        df = pd.DataFrame({
            "Classe de Ativo": ["Caixa", "Títulos Públicos", "Hipotecas", "Corp. IG", "High-Yield", "Não Classificado"],
            "Alocação ($M)": [cash, gov_bonds, mortgages, corp_loans, high_yield, unrated],
            "Peso de Risco": [0, 0.1, 0.5, 1.0, 1.2, 1.5],
            "RWA Contribuição ($M)": [0, gov_bonds*0.1, mortgages*0.5, corp_loans*1.0, high_yield*1.2, unrated*1.5]
        })
        
        st.dataframe(df, use_container_width=True)
    
    with col2:
        st.subheader("Dashboard em Tempo Real")
        
        fig_pie = px.pie(df, values="Alocação ($M)", names="Classe de Ativo", title="Composição do Portfólio")
        st.plotly_chart(fig_pie, use_container_width=True)
        
        fig_bar = px.bar(df, x="Classe de Ativo", y="RWA Contribuição ($M)", title="Contribuição para RWA")
        st.plotly_chart(fig_bar, use_container_width=True)
        
        st.metric("Ativos Totais", f"${total_assets}M")
        st.metric("RWA Total", f"${rwa/1e6:.1f}M")
        st.metric("Capital Mínimo Exigido (8%)", f"${required_capital/1e6:.1f}M")
        
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = car,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Capital Adequacy Ratio (CAR)"},
            delta = {'reference': 10.5},
            gauge = {
                'axis': {'range': [None, 25]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 8], 'color': "red"},
                    {'range': [8, 10.5], 'color': "orange"},
                    {'range': [10.5, 25], 'color': "green"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 8}}))
        st.plotly_chart(fig_gauge)
        
        if car >= 10.5:
            st.success("✅ Banco bem capitalizado!")
        elif car >= 8:
            st.warning("⚠️ Acima do mínimo, mas abaixo do buffer recomendado")
        else:
            st.error("❌ Ratio abaixo do mínimo regulatório!")

# ==================== MÓDULO 2: SIMULADOR DE RISCO DE CRÉDITO ====================
elif modulo == "2️⃣ Simulador de Risco de Crédito":
    st.header("Módulo 2: Provisões e Ciclo de Crédito")
    st.markdown("**Objetivo**: ver na prática por que o IFRS 9 reduz a prociclicidade e cria colchão antes da crise")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Configuração Inicial")
        carteira = st.number_input("Carteira de empréstimos ($M)", 100, 2000, 500)
        taxa_juros = st.slider("Taxa média de juros anual (%)", 10.0, 25.0, 15.0)
        cenario = st.selectbox("Cenário econômico", ["Boom", "Normal", "Recessão"])
        modelo = st.radio("Modelo de provisionamento", ["IAS 39 (perda incorrida)", "IFRS 9 (perda esperada)"])

    # Taxas de inadimplência (PD) por cenário
    if cenario == "Boom":
        pd_rates = [0.5, 0.4, 0.3, 0.4, 0.5]
    elif cenario == "Normal":
        pd_rates = [1.0, 1.2, 1.5, 1.8, 1.6]
    else:  # Recessão
        pd_rates = [2.0, 3.5, 6.0, 12.0, 8.0]  # pico de 12 %

    anos = [2025, 2026, 2027, 2028, 2029]
    lgd = 0.5
    realized_loss = [carteira * (pd / 100) * lgd for pd in pd_rates]
    total_realized = sum(realized_loss)

    # Provisão base (12-month ECL ≈ 1 % da carteira para IFRS 9 mesmo em bons tempos)
    base_ifrs9 = carteira * 0.01  # 1 % ao ano (ajuste se quiser mais/menos dramático)

    if cenario == "Recessão":
        front_proportions = [0.35, 0.30, 0.20, 0.10, 0.05]  # IFRS 9 antecipa forte
        back_proportions = [0.00, 0.05, 0.15, 0.35, 0.45]   # IAS 39 “cliff” no final

        if modelo == "IFRS 9 (perda esperada)":
            provisao = [round(base_ifrs9 + total_realized * p, 1) for p in front_proportions]
        else:
            provisao = [round(0 + total_realized * p, 1) for p in back_proportions]
    else:
        # Em Boom/Normal o IFRS 9 sempre provisiona mais (conservadorismo)
        if modelo == "IFRS 9 (perda esperada)":
            provisao = [round(base_ifrs9, 1) for _ in anos]
        else:
            provisao = [0.0 for _ in anos]  # IAS 39 quase nada em bons tempos

    juros_anual = carteira * (taxa_juros / 100)
    juros = [round(juros_anual, 1) for _ in anos]

    lucro = [round(j - p, 1) for j, p in zip(juros, provisao)]

    df_sim = pd.DataFrame({
        "Ano": anos,
        "Juros ($M)": juros,
        "Provisões ($M)": provisao,
        "Lucro Líquido ($M)": lucro
    })
    
    st.subheader("Simulação 5 anos")
    st.dataframe(df_sim, use_container_width=True)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=anos, y=juros, name="Receita de Juros", marker_color="#00cc96"))
    fig.add_trace(go.Bar(x=anos, y=[-p for p in provisao], name="Provisões", marker_color="#ff4444"))
    fig.update_layout(barmode="relative", title="Receita de Juros × Provisões", yaxis_title="$ milhões")
    st.plotly_chart(fig, use_container_width=True)
    
    st.metric("Provisões Cumulativas", f"${sum(provisao):.1f}M")
    st.metric("Lucro Acumulado", f"${sum(lucro):.1f}M")
    
    if cenario != "Recessão":
        if modelo == "IFRS 9 (perda esperada)":
            st.info("💡 Em tempos bons o IFRS 9 já provisiona mais que o IAS 39 → constroem colchão antecipado")
        else:
            st.info("📌 IAS 39 praticamente não provisiona em bons tempos (só quando a perda já ocorreu)")
    else:
        if modelo == "IFRS 9 (perda esperada)":
            st.success("✅ IFRS 9 antecipa a perda esperada → cria colchão antes da recessão e estabiliza lucro")
        else:
            st.warning("⚠️ IAS 39: “cliff effect” → lucro inflado no início, depois colapso (crise 2008)")

# ==================== MÓDULO 3: ALAVANCAGEM ====================
elif modulo == "3️⃣ Alavancagem x Capital Baseado em Risco":
    st.header("Módulo 3: As Duas Restrições Simultâneas")
    st.markdown("Todo banco enfrenta **dois limites**: Capital baseado em risco (CAR, ou Índice de Basileia) e Índice de Alavancagem")
    
    capital = st.number_input("Capital próprio ($M)", 50, 300, 100)
    ativos_totais = st.slider("Ativos totais ($M)", 500, 5000, 1500)
    rwa_percent = st.slider("% dos ativos que são RWA", 40, 100, 70)
    
    rwa = ativos_totais * (rwa_percent / 100)
    car = (capital / rwa) * 100 if rwa > 0 else 0
    leverage = (capital / (ativos_totais)) * 100
    
    col1, col2 = st.columns(2)
    with col1:
        fig1 = go.Figure(go.Indicator(mode="gauge+number", value=car, title={'text': "CAR, Índice de Basileia (%)"}, 
                                     gauge={'axis': {'range': [0, 25]}, 'threshold': {'value': 10.5}}))
        st.plotly_chart(fig1)
    with col2:
        fig2 = go.Figure(go.Indicator(mode="gauge+number", value=leverage, title={'text': "Índice de Alavancagem (%)"}, 
                                     gauge={'axis': {'range': [0, 15]}, 'threshold': {'value': 3}}))
        st.plotly_chart(fig2)
    
    if car < 10.5 and leverage >= 3:
        st.error("Banco em situação crítica - viola ambas as regras!")
    elif leverage < 3 and car < 10.5:
        st.error("Restrição ativa: Requerimento Mínimo de Capital não satisfeito")
    elif car >= 10.5 and leverage >= 3:
        st.error("Restrição ativa: Índice de Alavancagem (ex: bancos com ativos em excesso, mas de baixo risco)")
    else:
        st.success("Banco cumpre ambas as exigências!")

# ==================== MÓDULO 4: SIMULAÇÃO INTEGRADA ====================
elif modulo == "4️⃣ Simulação Integrada - Construa seu Banco":
    st.header("Módulo 4: Construa seu Banco!")

    # Inicialização única
    if 'ano_atual' not in st.session_state:
        st.session_state.ano_atual = 2025
        st.session_state.capital = 150.0
        st.session_state.ativos = 1000.0
        st.session_state.rwa_percent = 70   # %  # valor em percentagem para exibição
        st.session_state.historico = []

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader(f"Ano {st.session_state.ano_atual}")
        crescimento = st.slider("Crescimento anual dos ativos (%)", -20, 60, 12, 1)
        roa = st.slider("ROA esperado (retorno sobre ativos %)", 0.0, 8.0, 4.0, 0.1) / 100
        provisao_stress = st.checkbox("Evento de stress/recessão neste ano?")

    # Cálculos do ano
    novo_ativo = round(st.session_state.ativos * (1 + crescimento / 100), 1)
    lucro_bruto = round(novo_ativo * roa, 1)
    payout = 0.5  # 50% do lucro é distribuído como dividendo
    dividendos = round(lucro_bruto * payout, 1)

    if provisao_stress:
        provisao = round(novo_ativo * 0.04, 1)  # stress forte
    else:
        provisao = round(novo_ativo * 0.008, 1)  # normal

    delta_capital = lucro_bruto - provisao - dividendos
    st.session_state.capital = round(st.session_state.capital + delta_capital, 1)
    st.session_state.ativos = novo_ativo

    rwa_ratio = st.session_state.rwa_percent / 100
    car = round(st.session_state.capital / (novo_ativo * rwa_ratio) * 100, 1)
    leverage = round(st.session_state.capital / novo_ativo * 100, 1)

    # Dashboard do ano corrente
    colm1, colm2, colm3 = st.columns(3)
    colm1.metric("Capital", f"${st.session_state.capital:.0f}M", f"{delta_capital:+.0f}M")
    colm2.metric("Ativos Totais", f"${novo_ativo:.0f}M")
    colm3.metric("RWA / Ativos", f"{st.session_state.rwa_percent}%")

    colm1, colm2, colm3 = st.columns(3)
    colm1.metric("CAR (Capital Adequacy Ratio)", f"{car}%", 
                 "🟢 OK" if car >= 10.5 else "🔴 Abaixo do requerido")
    colm2.metric("Leverage Ratio", f"{leverage}%", 
                 "🟢 OK" if leverage >= 3 else "🔴 Abaixo do requerido")
    colm3.metric("ROA realizado", f"{roa*100:.1f}%")

    st.metric("Dividendos pagos", f"50% do lucro → ${dividendos}M")

    # Botão de avanço
    if st.button("➡️ Avançar para o próximo ano", type="primary"):
        st.session_state.historico.append({
            "Ano": st.session_state.ano_atual,
            "Capital": st.session_state.capital,
            "Ativos": novo_ativo,
            "CAR": car,
            "Leverage": leverage,
            "RWA %": st.session_state.rwa_percent
        })
        st.session_state.ano_atual += 1

        if st.session_state.ano_atual > 2027:
            st.success("🎉 Simulação de 3 anos concluída!")
            st.balloons()
            if car >= 10.5 and leverage >= 3:
                st.success("🏦 Seu banco sobreviveu e está bem capitalizado!")
            else:
                st.error("💥 Seu banco violou requisitos regulatórios – intervenção regulatória")
        st.rerun()

    # Gráfico histórico
    if st.session_state.historico:
        df_hist = pd.DataFrame(st.session_state.historico)
        fig = px.line(df_hist, x="Ano", y="CAR", markers=True, title="Evolução do CAR")
        fig.add_hline(y=10.5, line_dash="dash", line_color="orange", annotation_text="Mínimo 10.5%")
        fig.add_hline(y=8.0, line_dash="dash", line_color="red", annotation_text="Mínimo regulatório")
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Botão de reinício (sempre visível no final da página)
    if st.button("🔄 Reiniciar Simulação Completa", type="secondary"):
        keys_to_del = ['ano_atual', 'capital', 'ativos', 'rwa_percent', 'historico']
        for k in keys_to_del:
            st.session_state.pop(k, None)
        st.success("Simulação reiniciada!")
        st.rerun()
        
# ==================== QUIZ & RECURSOS ====================
else:
    st.header("🧠 Quiz Final & Recursos")
    
    st.success("Parabéns por chegar até aqui! Teste seu conhecimento:")
    
    with st.form("quiz"):
        q1 = st.radio("Qual o capital mínimo exigido pelo Basel III (Pilar 1)?", ["4%", "8%", "10.5%"])
        q2 = st.radio("O que o Leverage Ratio tenta evitar?", ["Risco de crédito", "Alavancagem excessiva independentemente do risco dos ativos", "Risco operacional"])
        q3 = st.checkbox("IFRS 9 é mais conservadora que IAS 39 em recessões")
        
        if st.form_submit_button("Ver resultado"):
            pontos = 0
            if q1 == "10.5%": pontos += 1
            if q2 == "Alavancagem excessiva independentemente do risco dos ativos": pontos += 1
            if q3: pontos += 1
            
            st.write(f"Você acertou {pontos}/3!")
    
    st.markdown("### 📚 Recursos Adicionais")
    st.markdown("- [Site oficial do BIS](https://www.bis.org/bcbs/basel3.htm)")
    st.markdown("- [Resumo Basel III - BCB](https://www.bcb.gov.br/estabilidadefinanceira/basileia3)")
    st.markdown("- Glossário completo de termos regulatórios")

# Footer
st.divider()

st.markdown(
    """
    <div style='text-align: center;'>
        <p style='font-size: 0.9em; color: gray;'>
            © 2025 Financial Regulation Teaching Tool | Developed for educational purposes
        </p>
        <p style='font-size: 0.9em; color: gray;'>
            Prof. José Américo – Coppead
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
