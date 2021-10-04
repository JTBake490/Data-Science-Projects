import streamlit as st
import numpy as np
import joblib

st.write('''
# Iris Classification Predictions
''')

st.sidebar.header('Iris Flower Parameters')

sepal_len = st.sidebar.slider('Sepal Length', 0.1, 8.0, 3.5, 0.1)
sepal_width = st.sidebar.slider('Sepal Width', 0.1, 5.0, 3.5, 0.1)
petal_len = st.sidebar.slider('Petal Length', 0.1, 7.0, 3.5, 0.1)
petal_width = st.sidebar.slider('Petal Width', 0.1, 3.0, 1.5, 0.1)
data = np.array([sepal_len, sepal_width, petal_len, petal_width]).reshape(1, -1)

st.subheader('User Input Parameters')
st.write(f'''
    * Sepal Length --> {sepal_len}
    * Sepal Width -->  {sepal_width}
    * Petal Length --> {petal_len}
    * Petal Width -->  {petal_width}
''')

with open('iris_model.joblib', 'rb') as model_file:
    model = joblib.load(model_file)

pred =  model.predict(data)
pred_proba = model.predict_proba(data)

iris_mapping = {}
iris_mapping[0] = 'Setosa'
iris_mapping[1] = 'Versicolor'
iris_mapping[2] = 'Virginica'

st.subheader('Prediction')
st.write(iris_mapping[pred[0]])

st.subheader('Prediction Probility')
st.write(f'''
Setosa --> {np.round(pred_proba[0][0], 3)}%\n
Versicolor --> {np.round(pred_proba[0][1], 3)}%\n
Virginica --> {np.round(pred_proba[0][2], 3)}%\n
''')
