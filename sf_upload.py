import streamlit as st

file = st.file_uploader("Drop your CSV here to load to Snowflake", type={"csv"})
