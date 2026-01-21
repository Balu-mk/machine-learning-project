import streamlit as st
import numpy as np
import pandas as pd
import joblib

model=joblib.load('model.pkl')
label=joblib.load('label.pkl')    #AQI
label2=joblib.load('label2.pkl')    #City

st.title("AQI STATUS PREDICTION")
st.write("FILL THE DETAILS TO PREDICT AQI STATUS")

# Get the cities that the model was actually trained on
available_cities = label2.classes_.tolist()

City=st.selectbox('SELECT A CITY', available_cities)  # Use only trained cities
PM_2_5=st.number_input('PM2.5 from 0.04 to 132.900',min_value=0.040000,max_value=132.900000,value=67.450488)
PM10=st.number_input('PM10 from 21.092 to 176.352',min_value=21.092500,max_value=176.352500,value=118.128196)
NO=st.number_input('NO from 0.02 to 34.61',min_value=0.020000,max_value=34.610000,value=17.574156)
NO2=st.number_input('NO2 from 0.01 to 67.19',min_value=0.010000,max_value=67.192500,value=28.560579)
NOx=st.number_input('NOx from 0.00 to 68.03',min_value=0.000000,max_value=68.032500,value=32.309248)
NH3=st.number_input('NH3 from 0.01 to 40.64',min_value=0.010000,max_value=40.640000,value=23.482260)
CO=st.number_input('CO from 0.00 to 3.465',min_value=0.00000,max_value=3.46500,value=2.248696)
SO2=st.number_input('SO2 from 0.010 to 27.19',min_value=0.010000,max_value=27.190000,value=14.531719)
O3=st.number_input('O3 from 0.01 to 75.71',min_value=0.010000,max_value=75.715000,value=34.491236)
Benzene=st.number_input('Benzene from 0.00 to 7.84',min_value=0.000000,max_value=7.840000,value=3.280680)
Toluene=st.number_input('Toluene from 0.00 to 19.830',min_value=0.000000,max_value=19.830000,value=8.700707)
Xylene=st.number_input('Xylene from 0.39 to 4.6750',min_value=0.395000,max_value=4.675000,value=3.070049)

City=label2.transform([City])[0]

if st.button('AQI STATUS'):
    pred = model.predict([[City,PM_2_5,PM10,NO,NO2,NOx,NH3,CO,SO2,O3,Benzene,Toluene,Xylene]])[0]

    status = label.inverse_transform([pred])[0]   # Get actual category string
    st.success(f"AQI Status: {status}")







