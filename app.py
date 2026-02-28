import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st



df=pd.read_csv("diabetes.csv")



st.sidebar.title("Navigation")
page=st.sidebar.radio("Go to",["Home","Visualization","ML Model 1", "ML Model 2"])


if page =="Home":
	st.write("Under Construction")
elif page =="Visulization":
	st.write("Under Construction")
elif page =="ML Model 1":
	st.write("Under Construction")
elif page =="ML model 2":
	st.write("Under Construction")
	
