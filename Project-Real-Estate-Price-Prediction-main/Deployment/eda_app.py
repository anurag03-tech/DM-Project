import os
import pandas as pd
from PIL import Image
import streamlit as st

def run_eda_app():
    st.subheader("Data Analysis")

    submenu = st.sidebar.selectbox("Submenu", ["Overview", "Plots"])
    
    # Read the CSV file
    try:
        df = pd.read_csv(os.path.join(os.path.dirname(__file__), "Final_Project.csv"))
    except FileNotFoundError:
        st.error("The CSV file was not found. Please check the file path.")
        return

    if submenu == "Overview":
        with st.expander("Dataset"):
            st.dataframe(df)

        with st.expander("Data Types"):
            st.dataframe(df.dtypes)

        with st.expander("Data Summary"):
            st.dataframe(df.describe().transpose())  # Transpose for better readability

        with st.expander("Location Distribution"):
            st.dataframe(df["Region"].value_counts().head(30))

    elif submenu == "Plots":
        with st.expander("Price Range Distribution"):
            img2 = Image.open(os.path.join("IMG", "Price_Range_Distribution.png"))
            st.image(img2)

        with st.expander("Price with respect to Floor"):
            img3 = Image.open(os.path.join("IMG", "Property_Floor_Numbers_Bar.png"))
            st.image(img3)

        with st.expander("Price with respect to Bedroom and Bathroom"):
            img4 = Image.open(os.path.join("IMG", "BednBath_Price_Bar.png"))
            st.image(img4)

        with st.expander("Price with respect to Property Age"):
            img5 = Image.open(os.path.join("IMG", "Price_Age_Distribution.png"))
            st.image(img5)

        with st.expander("Price with respect to SqFt Area"):
            img6 = Image.open(os.path.join("IMG", "SqFt_Area_Price_Scatter.png"))
            st.image(img6)

        with st.expander("Central Mumbai Property Price"):
            img7 = Image.open(os.path.join("IMG", "Central Mumbai.png"))
            st.image(img7)

        with st.expander("South Mumbai Property Price"):
            img8 = Image.open(os.path.join("IMG", "South Mumbai.png"))
            st.image(img8)

        with st.expander("Thane Property Price"):
            img9 = Image.open(os.path.join("IMG", "Thane.png"))
            st.image(img9)
