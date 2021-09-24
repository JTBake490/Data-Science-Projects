import numpy as np
import pickle
from flask import Flask, request, render_template


app = Flask(__name__)
with open('shuttle_model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)[0]
    probabilities = [f'Class{idx}: ' + str(np.round(perc*100, 4)) + '%' for idx, perc in enumerate(model.predict_proba(final_features)[0], start=1)]

    class1, class2, class3, class4, class5, class6, class7 = probabilities

    return render_template('index.html', prediction_text=f'Predicted Class: {prediction}', class1=class1, class2=class2, class3=class3, class4=class4, class5=class5, class6=class6, class7=class7)

if __name__ == "__main__":
    import webbrowser
     
    webbrowser.get('firefox').open('localhost:5000')
    app.run()