import pickle
from PIL import Image
import streamlit as st
import streamlit.components.v1 as stc

# importing the smaller apps
from ml_app import run_ml_app
from eda_app import run_eda_app

html_temp = """
			<div style="background-color:black ;padding:05px;border-radius:10px;">
			<h1 style="color:white;text-align:center;">Housing Price Prediction</h1>
			</div>
			"""

def main():
	stc.html(html_temp)

	menu = ["Prediction", "Data Analysis"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice=="Data Analysis":
		run_eda_app()
	elif choice == "Prediction":
		run_ml_app()

main()