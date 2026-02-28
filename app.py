import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st



array=np.arange(1,769)
df=pd.read_csv("diabetes.csv")
df.index=array
df.index.name="Patient ID"




st.sidebar.title("Navigation")
page=st.sidebar.radio("Go to",["Home","Visualization","ML Model 1", "ML Model 2"])

if page == "Home":
	st.title("Diabetes Prediction App")
	st.write("Use the Sidebar to navigate through the site.")
	st.write("Heres a glimpse of the dataset:")
	#st.write(df.head())
	st.dataframe(df.head())
	st.dataframe(df.describe())

	with st.expander("Read More"):
		st.write("This dataset contains information about patients with diabetes. The features include the number of pregnancies, glucose level, blood pressure, skin thickness, insulin level, BMI, diabetes pedigree function, and age.")


elif page == "Visualization":
	st.title("Let's take a look!")
	st.write("choose a figure to visualize:")

	if st.button("Display Age Distribution Histogram"):
		st.title("Age Distribution of Patients")
		fig, ax = plt.subplots()
		ax.hist(df["Age"], bins=20, color='blue', edgecolor='black')
		ax.set_xlabel("Age")
		ax.set_ylabel("Counts")
		st.pyplot(fig)
		  
	
	

elif page == "ML Model 1":
	st.write("Under Construction")
elif page == "ML Model 2":
	st.write("Under Construction")
	
