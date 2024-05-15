"""
This module contains functions for loading and working with laptop clustering data.
"""

import pandas as pd
import streamlit as st


@st.cache_data
def load_data() -> pd.DataFrame:
    """
    Loads data from a CSV file containing information about laptops clusters and returns
    a Pandas DataFrame.
    Returns:
        pd.DataFrame: A DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(filepath_or_buffer='./datasets/processed/laptops_clusters.csv')


# Load data
df = load_data()

# Sidebar header
st.sidebar.header(body="Filters")

# Select model option
model = st.sidebar.selectbox(
    label="Select Model", options=df['model'].unique())

# Filter data
df_laptops_model = df[df['model'] == model]

# Filter cluster
df_laptops_final = df[df['cluster'] == df_laptops_model.iloc[0]['cluster']]

# Display data
st.write("Model Recomendations")
st.table(data=df_laptops_final)
