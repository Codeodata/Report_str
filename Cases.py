import pandas as pd #pip install pandas openpyxl
import streamlit  as st # pip install streamlit
from app import get_data_from_excel


def cases():
    df = get_data_from_excel()
    st.dataframe(df)
