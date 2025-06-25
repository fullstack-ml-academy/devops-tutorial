import os
import random

import pandas as pd
import pickle

# Einladen des trainierten Modells
model_name = "regressor_mpg.pickle"
file_path = os.path.join("data", "models")
file_to_open = open(os.path.join(file_path, model_name), "rb")
trained_model = pickle.load(file_to_open)
file_to_open.close()

# Feature im Model
features = trained_model.feature_names_in_

# Erstellen einer neuen Instanz
data = pd.read_csv(os.path.join("data", "auto-mpg.csv"), sep=";")

# Neue Instanz mit plausiblen Werten
feature_values = {}
for feature in features:
    feature_values[feature] = random.uniform(data[feature].min(), data[feature].max())

new_instance = pd.Series(feature_values)
print("Predict the mpg for the following values:")
print(new_instance)
# Ausgabe des Ergebnisses
prediction = trained_model.predict(new_instance.to_numpy().reshape(1, -1))[0]
print(f"Predicted mpg for these values is {prediction}.")
