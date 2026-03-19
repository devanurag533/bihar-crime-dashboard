import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Bihar Data Insights App")
st.write("Developed by: Anurag Kumar")

try:
    df = pd.read_csv('crime.csv')
    st.success("Data Load Ho Gaya!")
    st.dataframe(df.head())
    
    # Ek chota sa graph app par dikhane ke liye
    st.bar_chart(df['Total Cases for Trial (Col.3 +Col.4) ( Col. 5 )'].head(5))
except:
    st.error("Pehle 'crime.csv' file upload kijiye!")
