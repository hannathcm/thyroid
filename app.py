import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from xgboost import XGBClassifier
app = Flask(__name__)
model = pickle.load(open('modelxgb3.pkl', 'rb'))
enc =  pickle.load(open('enc.pickle','rb'))

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    prediction = prediction.astype(int)
    #output = round(prediction[0], 2)
    output=enc.inverse_transform(prediction)
    output=enc.inverse_transform(prediction)

    return render_template('index1.html', prediction_text='thyroid detction result is {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True,port=7000)