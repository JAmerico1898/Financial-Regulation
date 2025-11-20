# Financial Regulation under the Basel Accord
## Interactive Learning Platform for Banking Capital Requirements

A comprehensive Streamlit-based educational application designed to demystify the Basel Accords (Basel I, II, III, and IV) and prudential banking regulations for finance students, regulators, and banking professionals.

---

## 📚 Overview

This interactive pedagogical tool transforms complex banking regulations into hands-on simulations and visual experiences. Students learn by doing: building bank portfolios, managing capital ratios, simulating economic crises, and understanding why regulatory frameworks like Basel III exist to prevent systemic banking failures.

### Why Basel Matters

The 2008 financial crisis exposed critical weaknesses in global banking systems: insufficient capital buffers to absorb losses from subprime mortgages led to cascading bank failures and economic collapse. The Basel Accords establish international standards to ensure banks maintain adequate capital relative to their risk exposures, protecting depositors and financial stability.

---

## 🎯 Learning Objectives

After completing this application, users will be able to:

✅ **Understand Risk-Weighted Assets (RWA)** - How different asset classes carry different risk weights  
✅ **Calculate Capital Adequacy Ratios** - The 8% minimum and 10.5% buffer requirements  
✅ **Compare Credit Provisioning Models** - IAS 39 (incurred loss) vs. IFRS 9 (expected loss)  
✅ **Analyze Leverage Constraints** - Why banks face both risk-based and absolute leverage limits  
✅ **Simulate Bank Management** - Make multi-year decisions balancing growth, profitability, and compliance  
✅ **Evaluate Regulatory Trade-offs** - Understand procyclicality and countercyclical buffers

---

## 🚀 Key Features

### 1. **Risk-Weighted Assets (RWA) Playground**
Interactive portfolio builder demonstrating how asset composition impacts capital requirements:
- **Asset Classes**: Cash, sovereign bonds, mortgages, corporate loans, high-yield debt, unrated assets
- **Risk Weights**: From 0% (cash) to 150% (unrated exposures)
- **Real-time Visualization**: Pie charts, bar charts, and CAR gauge meters
- **Regulatory Thresholds**: Visual indicators for 8% minimum and 10.5% buffer

### 2. **Credit Risk Simulator**
Compare provisioning methodologies across economic cycles:
- **IAS 39 (Incurred Loss)**: Recognize losses only when defaults occur
- **IFRS 9 (Expected Loss)**: Forward-looking provisioning based on probability of default (PD)
- **Scenario Analysis**: Boom, normal, and recession cycles
- **Procyclicality Demonstration**: See how IFRS 9 creates buffers before crises

### 3. **Leverage vs. Risk-Based Capital**
Understand the dual constraint framework:
- **Capital Adequacy Ratio (CAR)**: Risk-weighted capital requirement (10.5% target)
- **Leverage Ratio**: Simple assets-to-capital constraint (3% minimum)
- **Binding Constraint Analysis**: Identify which regulation is limiting for different bank profiles
- **Visual Gauges**: Real-time compliance monitoring

### 4. **Integrated Bank Simulation**
Multi-year strategic management game:
- **Annual Decision-Making**: Set growth rates, ROA targets, and dividend policies
- **Crisis Management**: Handle economic stress events requiring increased provisioning
- **Capital Dynamics**: Balance retained earnings, dividends, and regulatory compliance
- **Historical Tracking**: Visualize CAR evolution over 3+ years
- **Success Metrics**: Survive regulatory scrutiny while maximizing shareholder value

### 5. **Knowledge Assessment**
Quiz module testing comprehension:
- Basel III minimum capital requirements
- Purpose of leverage ratios
- IFRS 9 vs. IAS 39 comparison
- Instant feedback and scoring

---

## 🛠️ Technical Stack

### Core Technologies
- **Streamlit**: Web application framework for interactive data apps
- **Python 3.7+**: Primary programming language
- **Pandas**: Data manipulation and financial calculations
- **NumPy**: Numerical operations for risk modeling
- **Plotly**: Interactive charts (gauges, time series, pie charts)

### Key Libraries
```python
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.23.0
plotly>=5.14.0
```

---

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager
- Virtual environment (recommended)

### Setup Instructions

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd basel-accord-explorer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run reg_prudencial.py
   ```

The app will open automatically at `http://localhost:8501`

---

## 🎮 Usage Guide

### Navigation

The application features a sidebar with six main modules:

1. **🏠 Introduction** - Context on Basel Accords and regulatory motivation
2. **1️⃣ Risk-Weighted Assets** - Portfolio composition and RWA calculation
3. **2️⃣ Credit Risk Simulator** - Provisioning models and loss recognition
4. **3️⃣ Leverage Analysis** - Dual constraint framework
5. **4️⃣ Bank Builder** - Integrated multi-year simulation
6. **🧠 Quiz & Resources** - Assessment and external links

### Module Workflows

#### Module 1: RWA Portfolio Builder
1. Allocate $100M across six asset classes using sliders
2. Observe real-time changes to RWA contribution
3. Monitor Capital Adequacy Ratio (CAR) gauge
4. Experiment with conservative vs. aggressive strategies

**Key Insight**: High-yield and unrated assets dramatically increase capital requirements even if they represent small portfolio fractions.

#### Module 2: Credit Provisioning Comparison
1. Set initial loan portfolio size ($100M-$2000M)
2. Choose interest rate and economic scenario
3. Compare IAS 39 vs. IFRS 9 provisioning
4. Observe the "cliff effect" in recession under IAS 39

**Key Insight**: IFRS 9's expected loss model creates pre-emptive buffers, reducing procyclicality during economic downturns.

#### Module 3: Leverage Constraints
1. Input bank capital ($50M-$300M)
2. Set total assets ($500M-$5000M)
3. Adjust RWA percentage (40%-100% of assets)
4. Identify which constraint binds

**Key Insight**: Risk-based capital (CAR) and leverage ratios can bind simultaneously or independently depending on asset risk profile.

#### Module 4: Integrated Bank Simulation
1. Start with $150M capital and $1000M assets
2. Each year, set:
   - Asset growth rate (-20% to +60%)
   - Expected ROA (0% to 8%)
   - Stress event toggle (increases provisioning to 4%)
3. System calculates:
   - Gross profit = Assets × ROA
   - Provisions based on scenario
   - Dividends (50% payout ratio)
   - Net capital change
4. Advance through multiple years
5. Monitor CAR and leverage compliance
6. Receive final assessment: survival or regulatory intervention

**Winning Strategy**: Balance growth ambitions with capital accumulation; avoid excessive dividends during stress periods.

---

## 📊 Regulatory Framework

### Basel III Capital Requirements

| **Component** | **Minimum** | **Target with Buffer** |
|---------------|-------------|------------------------|
| Common Equity Tier 1 (CET1) | 4.5% | 7.0% |
| Tier 1 Capital | 6.0% | 8.5% |
| Total Capital | 8.0% | 10.5% |
| Leverage Ratio | 3.0% | 3.0% |

### Risk Weight Examples (Standardized Approach)

| **Asset Class** | **Risk Weight** |
|-----------------|-----------------|
| Cash and central bank reserves | 0% |
| AAA sovereign bonds | 0-20% |
| Residential mortgages | 35-75% |
| Corporate loans (investment grade) | 100% |
| High-yield corporate debt | 100-150% |
| Unrated/defaulted exposures | 150% |

### IFRS 9 Three-Stage Model

- **Stage 1**: Performing loans → 12-month expected loss provision
- **Stage 2**: Significant credit deterioration → Lifetime expected loss
- **Stage 3**: Credit-impaired → Lifetime expected loss + interest suspension

---

## 🎓 Pedagogical Approach

### Active Learning Design
This application follows evidence-based teaching principles:

1. **Learning by Doing**: Students manipulate variables and observe consequences
2. **Immediate Feedback**: Visual gauges and color-coded alerts provide instant reinforcement
3. **Scaffolded Complexity**: Modules build from simple concepts (RWA) to integrated scenarios (bank management)
4. **Real-World Context**: Case references to 2008 crisis and current regulations
5. **Formative Assessment**: Quiz validates comprehension

### Target Audiences

**Academic Settings**
- MBA finance courses
- Banking and financial regulation modules
- Risk management programs
- Central bank training academies

**Professional Development**
- Bank internal compliance training
- Regulatory authority onboarding
- Audit firm risk assessment teams
- Investment analysts covering financials

---

## 📈 Key Calculations

### Capital Adequacy Ratio (CAR)
```python
RWA = Σ(Asset_i × Risk_Weight_i)
CAR = (Total_Capital / RWA) × 100%
Minimum = 8%, Target with Buffer = 10.5%
```

### Leverage Ratio
```python
Leverage_Ratio = (Tier_1_Capital / Total_Assets) × 100%
Minimum = 3%
```

### IFRS 9 Expected Loss
```python
Expected_Loss = Exposure_at_Default × Probability_of_Default × Loss_Given_Default
Provision = Expected_Loss (Stage 1: 12m, Stage 2/3: Lifetime)
```

### Bank Capital Dynamics
```python
Capital(t+1) = Capital(t) + Net_Income - Dividends
Net_Income = Interest_Income - Provisions - Operating_Expenses
```

---

## 🔍 Educational Insights

### Module 1 Insights: RWA Mechanics
- **Conservative Bank**: High allocation to cash/sovereigns → Low RWA → Easy compliance but low profitability
- **Aggressive Bank**: High allocation to corporates/high-yield → High RWA → Requires more capital
- **Optimal Strategy**: Balance risk-return while maintaining regulatory buffers

### Module 2 Insights: Provisioning Models
- **IAS 39 Problem**: Procyclical - provisions surge during crises when capital is scarce
- **IFRS 9 Solution**: Provisions built during good times create "rainy day" funds
- **Trade-off**: IFRS 9 reduces earnings volatility but requires sophisticated forecasting

### Module 3 Insights: Dual Constraints
- **When CAR Binds**: Banks with risky assets hit risk-based limit first
- **When Leverage Binds**: Banks with massive low-risk assets (e.g., government bonds) hit absolute leverage limit
- **Regulatory Intent**: Leverage ratio prevents gaming via low-risk-weight assets

### Module 4 Insights: Strategic Management
- **Capital Generation**: Retained earnings are the cheapest capital source
- **Growth Constraint**: Rapid asset expansion requires capital raises or dividend cuts
- **Stress Response**: Conservative banks with buffers survive crises; overleveraged banks fail

---

## 🌍 Real-World Context

### Historical Motivation

**Pre-2008 Failures**
- Many banks operated with <4% capital ratios
- Risk weights underestimated mortgage and structured product risks
- Insufficient buffers led to taxpayer bailouts

**Post-Crisis Reforms**
- Basel III (2010): Raised minimum capital, introduced leverage ratio
- IFRS 9 (2018): Forward-looking provisioning to reduce procyclicality
- Basel IV (2023): Revisions to risk-weight calculations

### Brazilian Implementation

The Central Bank of Brazil (BCB) implements Basel standards through:
- **Resolution 4,193/2013**: Basel III capital requirements
- **Resolution 4,557/2017**: Liquidity Coverage Ratio (LCR)
- **BACEN Circular 3,691**: Standardized approach for credit risk

---

## 🚧 Limitations & Extensions

### Current Limitations
- Simplified risk weights (full Basel uses internal models)
- No market risk or operational risk modules
- Static loan portfolio (no amortization or defaults)
- Single-jurisdiction focus (no cross-border complexities)

### Potential Enhancements
- **Pillar 2 Add-on**: Supervisory review and stress testing
- **Pillar 3 Disclosure**: Public reporting requirements
- **Liquidity Ratios**: LCR and NSFR implementation
- **Internal Ratings**: IRB approach for credit risk
- **Market Risk**: Trading book and VaR calculations
- **Stress Testing**: Adverse scenario simulations
- **Multi-period Planning**: 5-10 year capital plans

---

## 📚 Additional Resources

### Official Documentation
- [Bank for International Settlements (BIS)](https://www.bis.org/bcbs/basel3.htm)
- [Basel Committee on Banking Supervision](https://www.bis.org/bcbs/)
- [Banco Central do Brasil - Basel III](https://www.bcb.gov.br/estabilidadefinanceira/basileia3)

### Academic References
- **Basel III: A Global Regulatory Framework** - BCBS, 2010
- **IFRS 9 and Expected Loss Provisioning** - EBA Report, 2016
- **Procyclicality of the Financial System** - Borio et al., BIS Working Paper

### Related Regulations
- **CRD IV/CRR** - European Union implementation
- **Dodd-Frank Act** - US regulatory framework
- **Resolution CMN 4,193** - Brazilian Basel III rules

---

## 👥 Credits & Acknowledgments

**Author**: Prof. José Américo  
**Institution**: Coppead - UFRJ Business School  
**Purpose**: Pedagogical tool for MBA and finance education  
**Year**: 2025

### Design Philosophy
This application embodies the principle that **"to understand regulation, you must experience its constraints."** By simulating the capital management challenge faced by real bank CFOs and risk officers, students develop intuition for why Basel frameworks exist and how they shape banking strategy.

---

## 📄 License

This educational tool is developed for academic purposes at Coppead/UFRJ. For usage rights, distribution, or adaptation, please contact the institution.

---

## 🤝 Feedback & Contributions

### For Instructors
This application works best when integrated into courses with:
- Pre-reading on Basel history and 2008 crisis
- Post-simulation discussion on strategic trade-offs
- Case studies of banks that violated capital requirements

### For Students
To maximize learning:
1. Complete modules sequentially (1→4)
2. Experiment with extreme scenarios (e.g., 100% high-yield portfolio)
3. Take notes on why certain strategies fail
4. Attempt the quiz without reviewing materials first

### Contact
For questions, bug reports, or suggestions for enhancements, reach out through Coppead/UFRJ academic channels.

---

## 🎯 Quick Start Checklist

- [ ] Install Python 3.7+ and dependencies
- [ ] Run `streamlit run reg_prudencial.py`
- [ ] Start with **🏠 Introduction** module
- [ ] Build a portfolio in **Module 1**
- [ ] Compare provisioning models in **Module 2**
- [ ] Understand dual constraints in **Module 3**
- [ ] Simulate 3 years of bank management in **Module 4**
- [ ] Test knowledge with **Quiz**
- [ ] Explore BIS/BCB documentation for deeper study

---

## 📞 Technical Support

### Common Issues

**Problem**: Gauges not rendering  
**Solution**: Update Plotly to latest version (`pip install --upgrade plotly`)

**Problem**: Import errors  
**Solution**: Verify all dependencies installed (`pip list`)

**Problem**: Simulation reset not working  
**Solution**: Refresh browser and clear Streamlit cache (`Ctrl+Shift+R`)

---

**🏦 Start your journey through global banking regulation – Build a bank, test its resilience, and understand why capital requirements are the cornerstone of financial stability!**
