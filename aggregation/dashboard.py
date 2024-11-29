import streamlit as st
import requests

# API URLs for aggregation
AGGREGATE_API_URL = "http://127.0.0.1:9000/aggregate"

st.title("Health Metrics Dashboard")

# Fetch insights from the aggregation API
st.subheader("Personalized Insights")
try:
    response = requests.get(AGGREGATE_API_URL, timeout=10)
    if response.status_code == 200:
        insights = response.json()
        for key, value in insights.items():
            st.write(f"**{key}:** {value}")
    else:
        st.error(f"Failed to fetch insights. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    st.error(f"Error connecting to the API: {e}")
