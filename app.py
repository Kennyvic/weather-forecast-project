import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import pickle
import base64
import joblib
from PIL import Image
import os


# Load the FUNAAB logo
funaab_logo = Image.open("C:/Users/Kent/Documents/weather project/funaab logo.png")


# Generate some dummy weather data for the next 10 years
date_range = pd.date_range(start="2024-01-01", end="2034-01-01", freq='D')
data = {
    "Date": date_range,
    "Rainfall (mm)": np.random.uniform(0, 20, size=len(date_range)),
    "Sunshine Hours": np.random.uniform(0, 12, size=len(date_range)),
    "Mean Temperature (°C)": np.random.uniform(15, 35, size=len(date_range)),
    "Weather Condition": np.random.choice(["Sunny", "Rainy", "Cloudy"], size=len(date_range))
}
df = pd.DataFrame(data)

# Streamlit app
st.set_page_config(page_title="Daily Weather Forecast", page_icon=":sunny:", layout="wide")

# Sidebar with FUNAAB logo and date selection
st.sidebar.image(funaab_logo, use_column_width=True)
st.sidebar.title("Weather Forecast")
start_date = st.sidebar.date_input("Start Date", value=date_range[0].date())
end_date = st.sidebar.date_input("End Date", value=date_range[10].date())

# Filter data based on selected date range
filtered_df = df[(df["Date"] >= np.datetime64(start_date)) & (df["Date"] <= np.datetime64(end_date))]

st.title("Today's Weather Forecast for FUNAAB Campus")
st.subheader(f"Weather data from {start_date} to {end_date}")

# Display weather data with pictorial descriptions
for i, row in filtered_df.iterrows():
    st.write(f"**Date:** {row['Date'].date()}")
    # st.image(icons[row["Weather Condition"]], width=50)
    st.write(f"**Rainfall:** {row['Rainfall (mm)']:.2f} mm")
    st.write(f"**Sunshine Hours:** {row['Sunshine Hours']:.2f} hours")
    st.write(f"**Mean Temperature:** {row['Mean Temperature (°C)']:.2f} °C")
    st.write("---")



# Convert the dictionary to a DataFrame
table_df = pd.DataFrame(data)

# Add some color and formatting
st.markdown(
    """
    <style>
    .stImage { margin-bottom: 10px; }
    .stTextInput>div>div { width: 100%; }
    </style>
    """, 
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .reportview-container {
        background: linear-gradient(to right, #f5f7fa, #c3cfe2);
        color: #333;
    }
    .sidebar .sidebar-content {
        background: #f7f7f7;
    }
    </style>
    """, 
    unsafe_allow_html=True
)