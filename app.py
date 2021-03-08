#import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# default page of our web-app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/suivi')
def suivi():
    return render_template('suivi.html')


@app.route('/consultations')
def consultations():
    return render_template('consultations.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


# To use the predict button in our web-app


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]

    return render_template('suivi.html', prediction_text='La décision finale est : {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
