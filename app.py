import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Page Config (Mobile Optimization)
st.set_page_config(page_title="Bihar Crime Tracker", layout="centered", page_icon="⚖️")

# 2. Custom CSS for Premium Look
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    div.stButton > button:first-child { background-color: #2e3b4e; color: white; border-radius: 5px; }
    .stMetric { background-color: white; padding: 20px; border-radius: 15px; border: 1px solid #e1e4e8; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .stTitle { color: #2e3b4e; font-family: 'Georgia', serif; font-size: 32px; font-weight: bold; }
    .stHeader { color: #50596c; }
    footer { visibility: hidden; }
    .reportview-container .main .footer { visibility: visible; }
    </style>
    """, unsafe_allow_html=True)

# 3. Premium Header
st.markdown("""
    <div style="background-color:#2e3b4e;padding:20px;border-radius:10px;text-align:center;margin-bottom:20px;">
        <h1 style="color:white;margin:0;font-size:28px;">📊 Bihar State Crime Dashboard</h1>
        <p style="color:#a1b1c7;margin:5px 0 0 0;font-size:14px;">Bihar Government Data Analysis (2023)</p>
    </div>
    """, unsafe_allow_html=True)

# 4. Data Loading and State-wise Check
try:
    df = pd.read_csv('crime.csv')
    
    # Check if 'District' column exists for state-wise analysis
    if 'District' in df.columns:
        st.sidebar.header("Filter Data")
        districts = df['District'].unique()
        selected_dist = st.sidebar.selectbox("Choose a District:", districts)
        filtered_df = df[df['District'] == selected_dist]
        st.subheader(f"📍 Analysis for {selected_dist} District")
    else:
        filtered_df = df # State-wise data analysis
        st.subheader("📍 Bihar State-wise Crime Summary")
        st.sidebar.warning("State-wise breakdown requires 'District' column in 'crime.csv'.")

    # 5. Stylish Metrics (Cards)
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    # Summing up key metrics from your CSV columns (adjust names if needed)
    total_ipc = filtered_df['Total IPC Crimes'].sum() if 'Total IPC Crimes' in filtered_df.columns else filtered_df['Cases Pending Trial from the Previous Year ( Col. 3 )'].sum()
    solved_cases = filtered_df['Cases Solved'].sum() if 'Cases Solved' in filtered_df.columns else 0 # Adjust based on actual column
    
    with col1:
        st.metric(label="📊 Total Reported Crimes (IPC)", value=f"{total_ipc:,}")
    with col2:
        st.metric(label="✅ Cases Successfully Solved", value=f"{solved_cases:,}")
        
    st.markdown("---")
    
    # 6. Smooth Bar Chart (Top 5 Crimes)
    st.subheader("📊 Top 5 Crime Categories")
    
    # Selecting relevant columns for the chart (adjust names if needed)
    if 'Crime Head ( Col. 2 )' in df.columns and 'Total IPC Crimes' in df.columns:
        chart_data = filtered_df[['Crime Head ( Col. 2 )', 'Total IPC Crimes']].head(5).set_index('Crime Head ( Col. 2 )')
        st.bar_chart(chart_data, color="#2e3b4e")
    else:
        st.bar_chart(filtered_df['Cases Pending Trial from the Previous Year ( Col. 3 )'].head(5))

except Exception as e:
    st.error(f"Error: {e}. Ensure 'crime.csv' is uploaded and column names match.")

# 7. Professional Footer (Mobile Friendly)
st.markdown("""
    <br><br>
    <div style="background-color:#f8f9fa;padding:20px;border-radius:10px;text-align:center;border-top: 1px solid #e1e4e8;margin-top:30px;">
        <p style="color:#50596c;margin:0;font-size:14px;">Powered by: <strong>Anurag Kumar</strong></p>
        <p style="color:#818ea0;margin:5px 0 0 0;font-size:12px;">Data Analyst Trainee | IIT Patna & Masai School</p>
        <p style="color:#818ea0;margin:5px 0 0 0;font-size:10px;">Data Source: OGD India Open Government Data</p>
    </div>
    """, unsafe_allow_html=True)
