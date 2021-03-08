#import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import random

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

    decision_finale = ""

    # 0 soins intensifs 1 go home 2 observation
    liste_0 = ['Après analyse de vos paramètres corporel, il est urgent de vous amener en soins intensifs', 'Désolé votre état de santé est critique, vous devez aller en soins intensifs',
               'Vous ne pouvez absolument pas sortir maintenant, votre état de santé est critique, vous devez directement aller en soins intensifs']
    liste_1 = ['Vos paramètres corporels sont stables, vous pouvez vous préparer à renter chez vous',
               "Vous avez l'air d'aller mieux, vous pouvez déjà renter chez vous", "Tout à l'air calme, vous pouvez renter chez vous sans aucune crainte"]

    liste_2 = ["Votre état s'est amélioré, mais vous ne pouvez pas encore entrer. Nous devons encore vous garder en observations quelquels temps",
               "Votre état est stable mais nous ne pouvons pas encore vous laiser rentrer chez vous. Nous devons vous garder en observations quelques temps pour se rassuer que tout va bien"]

    if output == 0:
        random.shuffle(liste_0)
        decision_finale = liste_0[0]
    elif output == 1:
        random.shuffle(liste_1)
        decision_finale = liste_1[0]
    elif output == 2:
        random.shuffle(liste_2)
        decision_finale = liste_2[0]

    return render_template('suivi.html', prediction_text='DECISION FINALE : {}'.format(decision_finale))


if __name__ == "__main__":
    app.run(debug=True)
