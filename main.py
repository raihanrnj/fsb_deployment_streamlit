import streamlit as st
import pandas as pd
import joblib
from PIL import Image

#Loading Our final trained Knn model 
model= open("models/Knn_Classifier.pkl", "rb")
knn_clf=joblib.load(model)


st.title("Iris flower species Classification App")

#Loading images

setosa= Image.open('assets/setosa.png')
versicolor= Image.open('assets/versicolor.png')
virginica = Image.open('assets/virginica.png')

st.sidebar.title("Features")

#Intializing
parameter_list=['sepal_length','sepal_width','petal_length','petal_width']
parameter_input_values=[]
parameter_default_values=['5.2','3.2','4.2','1.2']

values=[]

#Display
for parameter, parameter_df in zip(parameter_list, parameter_default_values):
	
	values= st.sidebar.slider(label=parameter, key=parameter,value=float(parameter_df), min_value=0.0, max_value=8.0, step=0.1)
	parameter_input_values.append(values)
	
input_variables=pd.DataFrame([parameter_input_values],columns=parameter_list,dtype=float)
st.write('\n\n')

if st.button("Click Here to Classify"):
	prediction = knn_clf.predict(input_variables)
	st.write(str(prediction[0]))
	if prediction == 'versicolor':
		st.image(versicolor)
	elif prediction == 'setosa':
		st.image(setosa)
	elif prediction == 'virginica':
		st.image(virginica)

	# st.image(setosa) if prediction == 0 else st.image(versicolor)  if prediction == 1 else st.image(virginica) 