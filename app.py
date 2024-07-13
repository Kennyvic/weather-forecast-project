import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import pickle
import base64
import joblib
import mplcursors

# Load the model
loaded_model = joblib.load('prophet_model.pkl')
