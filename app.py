# Import all the required libs
import streamlit as st
import pandas as pd
import numpy as np

# Add the data URL
DATA_URL = (
  "./data.csv"
)

# Add a title
st.title('Motor vehicle collisions in NYC')
st.markdown('''
  ### This web app is a streamlit dashboard 📈📊
  > Used to analyze the vehicle collisions in NYC 🗽
''')

@st.cache(persist=True)
def load_data(nrows):
  data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
  data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
  lowercase = lambda x: str(x).lower()
  data.rename(lowercase, axis='columns', inplace=True)
  data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)

  return data

data = load_data(100_000)

if st.checkbox('Show Raw Data 📝', False):
  st.subheader('Raw Data')
  st.write(data)
