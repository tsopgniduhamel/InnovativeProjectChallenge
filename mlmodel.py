
'''
This is a simple linear regression model to predit the CO2 emmission from cars
Dataset:
FuelConsumption.csv, which contains model-specific fuel consumption ratings and estimated carbon dioxide emissions
for new light-duty vehicles for retail sale in Canada
'''

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPClassifier
import pickle

donnees = pd.read_csv("PO_Generated_Data.data")
donnees.drop(['key_PO'], axis=1, inplace=True)

# # take a look at the dataset
# #df.head()

# #use required features
# cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]

# #Training Data and Predictor Variable
# # Use all data for training (tarin-test-split not used)
# x = cdf.iloc[:, :3]
# y = cdf.iloc[:, -1]

x = donnees[['L-CORE_C', 'L-SURF_C', 'L-O2_C', 'L-BP_C',
             'SURF-STBL_C', 'CORE-STBL_C', 'BP-STBL_C']]
y = donnees['decision_C']


modele_final = MLPClassifier(random_state=90, max_iter=250)

# Fitting model with trainig data
modele_final.fit(x, y)

# Saving model to disk
# Pickle serializes objects so they can be saved to a file, and loaded in a program again later on.
pickle.dump(modele_final, open('model.pkl', 'wb'))

'''
#Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2.6, 8, 10.1]]))
'''
