import streamlit as st
import pandas as pd
import json

file = st.file_uploader("Drop your CSV here to load to Snowflake", type={"csv"})
