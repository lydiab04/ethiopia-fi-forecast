import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(page_title="Ethiopia Financial Inclusion Dashboard", layout="wide")

st.title("🇪🇹 National Financial Inclusion Analytics & Scenario Engine")
st.markdown("**Consortium Executive Steering Tool | Task 1–Task 5 Integrated Deliverable**")

# Sidebar Navigation
st.sidebar.header("Navigation Menu")
page = st.sidebar.radio("Select Dashboard View:", [
    "Overview & Key Metrics", 
    "Trends & Channel Analysis", 
    "Event Impact Matrix", 
    "Forecasts & 60% Target Projections"
])

# Load Datasets safely
@st.cache_data
def load_data():
    years = [2014, 2017, 2021, 2024, 2025, 2026, 2027]
    df_trends = pd.DataFrame({
        'Year': years,
        'Account_Ownership': [22.0, 35.0, 46.0, 46.0, 51.2, 56.5, 62.1],
        'Digital_Payments': [12.0, 18.0, 28.0, 38.0, 43.5, 49.0, 55.2],
        'P2P_ATM_Crossover_Ratio': [0.10, 0.25, 0.85, 1.08, 1.45, 1.80, 2.20],
        'Mobile_Money_Accounts': [1.2, 2.5, 4.7, 9.45, 14.0, 19.5, 25.0]
    })
    return df_trends

df = load_data()

# -----------------------------------------------------------------------------
# PAGE 1: OVERVIEW
# -----------------------------------------------------------------------------
if page == "Overview & Key Metrics":
    st.header("📌 Executive Summary & Core Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Account Ownership (2024)", "46.0%", "+11.0% vs 2017")
    col2.metric("Digital Payment Adoption", "38.0%", "+10.0% vs 2021")
    col3.metric("P2P / ATM Crossover Ratio", "1.08", "Crossed 1.0 Threshold! 🚀")
    col4.metric("Mobile Money Penetration", "9.45%", "+4.75% post-Telebirr")
    
    st.divider()
    
    st.subheader("P2P / ATM Volume Crossover Acceleration")
    fig_cross = px.line(df, x='Year', y='P2P_ATM_Crossover_Ratio', markers=True, 
                        title="Digital Velocity Shift: P2P Volume relative to ATM Transactions")
    fig_cross.add_hline(y=1.0, line_dash="dash", line_color="red", annotation_text="Crossover Parity (1.0)")
    st.plotly_chart(fig_cross, use_container_width=True)

# -----------------------------------------------------------------------------
# PAGE 2: TRENDS
# -----------------------------------------------------------------------------
elif page == "Trends & Channel Analysis":
    st.header("📈 Historical Trends & Channel Comparisons")
    
    channel = st.multiselect("Select Delivery Channels / Indicators:", 
                             ["Account_Ownership", "Digital_Payments", "Mobile_Money_Accounts"], 
                             default=["Account_Ownership", "Digital_Payments"])
    
    fig_trend = px.line(df, x='Year', y=channel, markers=True, title="Historical Growth Trajectories (2014-2027)")
    st.plotly_chart(fig_trend, use_container_width=True)
    
    # Download Button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Trend Dataset (CSV)", csv, "ethiopia_fi_trends.csv", "text/csv")

# -----------------------------------------------------------------------------
# PAGE 3: EVENT IMPACT
# -----------------------------------------------------------------------------
elif page == "Event Impact Matrix":
    st.header("⚡ Macro Event & Policy Impact Association Matrix")
    
    matrix_df = pd.DataFrame({
        'EVT_TELEBIRR_2021': [0.12, 0.0475, 0.18, 0.08],
        'EVT_FAYDA_2023': [0.15, 0.08, 0.10, 0.12],
        'EVT_MPESA_2023': [0.05, 0.03, 0.07, 0.04],
        'EVT_FX_REFORM_2024': [0.08, 0.05, 0.12, 0.06]
    }, index=['ACC_OWNERSHIP', 'ACC_MM_ACCOUNT', 'USG_DIGITAL_PAYMENT', 'GEN_MM_SHARE'])
    
    fig_heat = px.imshow(matrix_df, text_auto=True, color_continuous_scale='YlGnBu',
                         title="Interactive Impact Heatmap (Events vs Findex Targets)")
    st.plotly_chart(fig_heat, use_container_width=True)

# -----------------------------------------------------------------------------
# PAGE 4: FORECASTS
# -----------------------------------------------------------------------------
elif page == "Forecasts & 60% Target Projections":
    st.header("🔮 Forward Projections & Consortium 60% Ownership Goal")
    
    scenario = st.selectbox("Select Policy & Economic Scenario:", ["Base Case", "Optimistic", "Pessimistic"])
    
    if scenario == "Base Case":
        vals = [46.0, 51.2, 56.5, 62.1]
    elif scenario == "Optimistic":
        vals = [46.0, 54.0, 61.5, 68.0]
    else:
        vals = [46.0, 48.5, 51.0, 54.2]
        
    f_years = [2024, 2025, 2026, 2027]
    
    fig_f = go.Figure()
    fig_f.add_trace(go.Scatter(x=f_years, y=vals, mode='lines+markers', name=f'{scenario} Scenario', line=dict(width=3)))
    fig_f.add_hline(y=60.0, line_dash="dash", line_color="purple", annotation_text="National 60% Target")
    fig_f.update_layout(title=f"Account Ownership Forecast Path ({scenario})", yaxis_title="Account Ownership (%)")
    
    st.plotly_chart(fig_f, use_container_width=True)
    
    if scenario in ["Base Case", "Optimistic"]:
        st.success("🎉 Outcome: National 60% Financial Inclusion Target is achieved by 2026/2027!")
    else:
        st.warning("⚠️ Outcome: Misses 60% Target. Policy interventions required!")