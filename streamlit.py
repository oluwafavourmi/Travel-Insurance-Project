import numpy as np
import pandas as pd
import pickle
import streamlit as st

#load the model 
loaded_model = pickle.load(open('trained model.pkl', 'rb'))

def Travel_Insurance_Prediction(Age, Employment_type, Graduate, Annual_income, Family_members, Chronic_diseases, Frequent_flyer, Ever_travelled_abroad):
    input_data_array = np.asarray([Age, Employment_type, Graduate, Annual_income, Family_members, Chronic_diseases, Frequent_flyer, Ever_travelled_abroad])
    reshaped_input = input_data_array.reshape(1, -1)
    prediction = loaded_model.predict(reshaped_input)

    return prediction



st.title('Travel Insurance Prediction')

Age = st.text_input('Enter Custormer Age')
Employment_type = st.text_input('Enter 0 for Government Job, 1 for Private sector')
Graduate = st.text_input('Enter 1 for graduate, 0 for non-graduate')
Annual_income = st.text_input('Enter Custormer annual income')
Family_members = st.text_input('Enter Custormer Family_size')
Chronic_diseases = st.text_input('Enter 1 for chronic diseases, 0 for no chronic diseases')
Frequent_flyer = st.text_input('Enter 1 for frequent flyer, 0 for not frequent flyer')
Ever_travelled_abroad = st.text_input('Enter 1 for ever travelled abroad, 0 for never travelled abroad')

final_pred = ''


if st.button('Travel insurance predict'):
    pred = Travel_Insurance_Prediction(Age, Employment_type, Graduate, Annual_income, Family_members, Chronic_diseases, Frequent_flyer, Ever_travelled_abroad)
    if (pred[0]==0):
        final_pred='this custormer will not buy the Insurance'
    else:
        final_pred = 'This custormer will buy the Insurance'

st.success(final_pred)
