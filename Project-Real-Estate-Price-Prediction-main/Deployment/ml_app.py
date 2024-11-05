import pickle
import numpy as np
import pandas as pd
import streamlit as st
import os

# Update paths for loading files
try:
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "Final_Project.csv"))
    with open(os.path.join(os.path.dirname(__file__), 'regression_model.pkl'), 'rb') as pickle_in:
        reg = pickle.load(pickle_in)
except FileNotFoundError as e:
    st.error(f"Error: {e}")
    st.stop()  # Stop execution if files are not found

def predict_price(Area_SqFt, Floor_No, Bedroom):
    x = np.zeros(7)
    
    x[0] = Area_SqFt
    x[1] = Floor_No
    x[2] = Bedroom

    return reg.predict([x])[0]

def run_ml_app():
    st.subheader('Select details :')
   
    col1, col2 = st.columns([1, 2])
    
    with col1:
        Location = st.selectbox('Select the Location', df['Region'].sort_values().unique())
    
    with col2:
        Area_SqFt = st.slider("Select Total Area in SqFt", 500, int(max(df['Area_SqFt'])), step=100)

    col3, col4 = st.columns(2)
    
    with col3:
        Floor_No = st.selectbox("Enter Floor Number", df['Floor_No'].sort_values().unique())
    
    with col4:
        Bathroom = st.selectbox("Enter Number of Bathroom", df['Bathroom'].sort_values().unique())

    col5, col6 = st.columns(2)
    
    with col5:
        Bedroom = st.selectbox("Enter Number of Bedroom", df['Bedroom'].sort_values().unique())
    
    with col6:
        Property_Age = st.selectbox('Select the Property Age', df['Property_Age'].sort_values().unique())
    
    result = ""
  
    if st.button("Calculate Price"):
        result = predict_price(Area_SqFt, Floor_No, Bedroom)
        
    st.success('Total Price in Lakhs : {}'.format(result))

if __name__ == '__main__':
    run_ml_app()
