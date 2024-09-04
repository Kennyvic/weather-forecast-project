import numpy as np
import pandas as pd
import streamlit as st
import base64
from PIL import Image
import uuid
import datetime

# Load the FUNAAB logo
funaab_logo = Image.open("funaab logo.png")

np.random.seed(42)

# Convert image to Base64
def image_to_base64(img):
    with open(img, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

funaab_logo_base64 = image_to_base64("funaab logo.png")

# Generate some dummy weather data for the next 10 years
date_range = pd.date_range(start="2024-01-01", end="2034-01-01", freq='D')
data = {
    "Date": date_range,
    "Rainfall (mm)": np.random.uniform(0, 20, size=len(date_range)),
    "Sunshine Hours": np.random.uniform(0, 12, size=len(date_range)),
    "Mean Temperature (°C)": np.random.uniform(15, 35, size=len(date_range)),
    "Evaporation (mm)": np.random.uniform(0, 10, size=len(date_range)),
    "Weather Condition": np.random.choice(["Sunny", "Rainy", "Cloudy"], size=len(date_range)),
}
df = pd.DataFrame(data)

# Streamlit app configuration
st.set_page_config(page_title="Daily Weather Forecast", page_icon=":sunny:", layout="wide")

# Sidebar with date selection
st.sidebar.title("Weather Forecast")
start_date = st.sidebar.date_input("Start Date", value=date_range[0].date())
end_date = st.sidebar.date_input("End Date", value=date_range[10].date())

# Filter data based on selected date range
filtered_df = df[(df["Date"] >= np.datetime64(start_date)) & (df["Date"] <= np.datetime64(end_date))]

# Round numeric columns to 2 decimal places
filtered_df[['Rainfall (mm)', 'Sunshine Hours', 'Mean Temperature (°C)', 'Evaporation (mm)']] = filtered_df[['Rainfall (mm)', 'Sunshine Hours', 'Mean Temperature (°C)', 'Evaporation (mm)']].round(2)

# Position the FUNAAB logo on the left and the title on the right
col1, col2 = st.columns([1.5, 4])  # Adjusted column widths

with col1:
    st.image(funaab_logo, width=150)  # Increased the image size

with col2:
    st.title("Today's Weather Forecast for FUNAAB Campus")

# Display today's date
current_date = datetime.datetime.now().strftime("%d/%m/%Y")
st.header(f"Today's date is: {current_date}")

# Filter the DataFrame for today's data
today_weather = df[df['Date'] == pd.to_datetime(current_date, format="%d/%m/%Y")]

# Convert icons to Base64
rainfall_icon_base64 = image_to_base64("icons/rain_icon.png")
sunshine_icon_base64 = image_to_base64("icons/sunshine_icon.jpeg")
temperature_icon_base64 = image_to_base64("icons/temperature_icon.png")
evaporation_icon_base64 = image_to_base64("icons/evaporation_icon.png")

# Display today's weather data with icons
st.markdown("### Today's Weather Data")

if not today_weather.empty:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f'<img src="data:image/png;base64,{rainfall_icon_base64}" width="50"/>', unsafe_allow_html=True)
        st.write(f"{today_weather['Rainfall (mm)'].values[0]:.2f} mm")
    
    with col2:
        st.markdown(f'<img src="data:image/png;base64,{sunshine_icon_base64}" width="50"/>', unsafe_allow_html=True)
        st.write(f"{today_weather['Sunshine Hours'].values[0]:.2f} hours")
    
    with col3:
        st.markdown(f'<img src="data:image/png;base64,{temperature_icon_base64}" width="50"/>', unsafe_allow_html=True)
        st.write(f"{today_weather['Mean Temperature (°C)'].values[0]:.2f} °C")
    
    with col4:
        st.markdown(f'<img src="data:image/png;base64,{evaporation_icon_base64}" width="50"/>', unsafe_allow_html=True)
        st.write(f"{today_weather['Evaporation (mm)'].values[0]:.2f} mm")
else:
    st.write("No weather data available for today.")

# Subheader for the filtered weather data
st.subheader(f"Weather data from {start_date} to {end_date}")

# Display the filtered DataFrame
st.write(filtered_df)

# Prepare CSV for download
uid = uuid.uuid4()
csv = filtered_df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()  # Base64 encode the CSV data
href = f'<a href="data:file/csv;base64,{b64}" download="weather_data_{uid}.csv">Download Weather Data as CSV</a>'
st.markdown(href, unsafe_allow_html=True)

# Add custom CSS for additional styling
st.markdown(
    """
    <style>
    .stImage { margin-bottom: 10px; }
    .stTextInput>div>div { width: 100%; }
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
