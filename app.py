from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
CORS(app)  # ✅ Autorise les requêtes du front

# ✅ Sécurisation contre les abus (DDoS, Bruteforce)
limiter = Limiter(get_remote_address, app=app, default_limits=["10 per minute"])

# ✅ Charger les données Titanic
titanic = sns.load_dataset('titanic')[['survived', 'pclass', 'sex', 'age']].dropna()
titanic['sex'] = titanic['sex'].replace({'male': 0, 'female': 1})

# ✅ Préparer les données
X = titanic[['pclass', 'sex', 'age']]
y = titanic['survived']

# ✅ Entraîner le modèle KNN
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X, y)

# ✅ Vérifier si l'API fonctionne
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API is running 🚀"})

# ✅ Endpoint sécurisé pour la prédiction
@app.route("/predict", methods=["POST"])
@limiter.limit("5 per minute")  # ✅ Max 5 requêtes par minute
def predict():
    data = request.get_json()

    # ✅ Vérifier si tous les champs sont présents
    if not all(k in data for k in ["sexe", "age", "classe"]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        # ✅ Vérifier les valeurs reçues
        sexe = 0 if data["sexe"] == "female" else 1
        age = int(data["age"])
        classe = int(data["classe"])

        if age < 1 or age > 100 or classe not in [1, 2, 3]:
            return jsonify({"error": "Invalid input values"}), 400

        # ✅ Faire la prédiction
        input_data = np.array([[classe, sexe, age]])
        prediction = model.predict(input_data)[0]
        result_message = "You survived! 🎉" if prediction == 1 else "You did not survive... 💀"

        return jsonify({"message": result_message})

    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input data"}), 400

# ✅ Démarrer l'API
if __name__ == "__main__":
    app.run(debug=True)
