import os
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import pickle

# Einlesen der CSV Datei
data = pd.read_csv("data/auto-mpg.csv", sep=";")

# Zielvariable bestimmen
y = data["mpg"]

# Alle anderen Variablen sind Einflussvariablen
X = data.loc[:, data.columns != "mpg"]

# Model definieren
regressor = DecisionTreeRegressor()

# Model trainieren
regressor = regressor.fit(X, y)

# Erstelle einen model Ordner in data falls dieser noch nicht existiert
file_path = os.path.join("data", "models")
os.makedirs(file_path, exist_ok=True)

# Abspeichern des Models
model_name = "regressor_mpg.pickle"
file_to_write = open(os.path.join(file_path, model_name), "wb")
pickle.dump(regressor, file_to_write)
