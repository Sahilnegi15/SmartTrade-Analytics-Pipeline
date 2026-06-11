import streamlit as st
import pandas as pd
from boto3 import client

athena = client('athena')
query = "SELECT order_date, SUM(revenue) as total_revenue FROM stap_dbt.fact_orders GROUP BY order_date"

st.title("STAP Dashboard")
st.line_chart(data)  