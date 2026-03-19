import streamlit as st
import pandas as pd

# 1. Page Config (Look and Feel)
st.set_page_config(page_title="Bihar Crime Insights", layout="wide", page_icon="⚖️")

# 2. Stylish Sidebar (Developer Info)
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/000000/data-configuration.png")
    st.title("Navigation")
    st.info("Analyze Bihar's crime data using this live dashboard.")
    st.markdown("---")
    st.write("👤 **Developer:** Anurag Kumar")
    st.write("🎓 **Affiliation:** IIT Patna & Masai")

# 3. Header
st.title("⚖️ Bihar District-wise Crime Insights")
st.markdown("---")

# 4. Data Loading
try:
    df = pd.read_csv('crime.csv')
    
    # Stylish Metrics (Boxes)
    col1, col2, col3 = st.columns(3)
    col1.metric("📊 Total Records", len(df))
    col2.metric("📍 Focus State", "Bihar")
    col3.metric("📈 Status", "Live ✅")

    st.markdown("---")
    
    # Two Columns for Table and Graph
    left_col, right_col = st.columns([1, 1])
    
    with left_col:
        st.subheader("📋 Data Table View")
        st.dataframe(df, use_container_width=True)
    
    with right_col:
        st.subheader("📊 Visual Trends")
        # Pending cases ka bar chart
        st.bar_chart(df['Cases Pending Trial from the Previous Year ( Col. 3 )'].head(10))

except Exception as e:
    st.error("Error: Please ensure 'crime.csv' is uploaded.")
