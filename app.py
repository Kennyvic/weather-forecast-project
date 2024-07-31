import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import pickle
import base64
import joblib


# Load the model
loaded_model = joblib.load('prophet_model.pkl')


def main():
    st.title('Daily Weather Forecast')
    st.write('Welcome to the daily weather forecast application. Here you can get the forecast for the day, and see the historical accuracy of our predictions.')

    # Add a selectbox to the sidebar:
    add_selectbox = st.sidebar.selectbox(
        'What would you like to do?',
        ('Get today\'s forecast', 'See historical accuracy')
    )

    if add_selectbox == 'Get today\'s forecast':
        st.write('Here is the forecast for today...')
        # Add code to run a prediction using your model
    elif add_selectbox == 'See historical accuracy':
        st.write('Here is the historical accuracy of our forecasts...')
        # Add code to display the historical accuracy of your model

if __name__ == "__main__":
    main()