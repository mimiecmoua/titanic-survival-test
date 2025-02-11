# 🚢 Titanic Survival Test 🚢

🧑‍💻 _By Émilie Clain - Développeuse Full-Stack & IA_

## 🎯 Description

Ce projet est une application web interactive qui permet de **prédire si un passager aurait survécu au naufrage du Titanic** en fonction de son **genre, son âge et sa classe sociale**.

L’application utilise **du Machine Learning** pour effectuer cette prédiction à partir d’un modèle basé sur **Scikit-Learn**.

### ✨ Fonctionnalités principales

- ✅ Sélection de l’âge, du genre et de la classe
- ✅ Envoi des données à une **API Flask**
- ✅ Prédiction en temps réel de la survie ou non du passager
- ✅ Interface responsive avec **Bootstrap 5**

---

## 🛠 Technologies utilisées

- **Frontend :** `HTML`, `CSS`, `JavaScript`, `Bootstrap`
- **Backend :** `Flask (Python)`, `Flask-CORS`
- **Machine Learning :** `Scikit-Learn (KNeighborsClassifier)`
- **Autres Librairies :** `Pandas`, `NumPy`, `Seaborn`

---

## 🚀 Installation & Exécution

### 📌 1️⃣ Cloner le projet

```bash
git clone https://github.com/mimiecmoua/titanic-survival-test.git
cd titanic-survival-test
```

### 📌 2️⃣ Installation des dépendances (API)

Assurez-vous d'avoir Python 3 et pip installés. Ensuite, exécutez :

```bash
Copier
Modifier
pip install -r requirements.txt
💡 (Ajoute un fichier requirements.txt avec toutes tes dépendances Python si besoin.)
```

### 📌 3️⃣ Lancer l’API Flask

```bash
Copier
Modifier
python app.py
L’API sera disponible sur : http://127.0.0.1:5000/
```

###

📌 4️⃣ Lancer le Frontend
Ouvrez simplement index.html dans votre navigateur OU servez-le avec un serveur local :

```bash
Copier
Modifier
python -m http.server
Accès : http://127.0.0.1:8000/
```

### 🖥️ API - Routes Disponibles

🔹 POST /predict
Permet d'envoyer les données du passager et retourne une prédiction.

### 📌 Exemple de requête avec curl :

```bash
Copier
Modifier
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"sexe\":\"female\", \"age\":25, \"classe\":1}"
```

📌 Réponse attendue :

```json
Copier
Modifier
{
    "message": "You survived! ❤️"
}
```

## 👩‍💻 Auteur

👤 Émilie Clain
🔗 Portfolio
🐙 GitHub
💼 LinkedIn

## 🌟 Licence

📜 Ce projet est sous licence MIT – Vous pouvez l’utiliser, le modifier et le partager librement. 🚀

### ✅ Dernière étape : Ajoute ce fichier et fais un dernier push sur GitHub !

```bash
Copier
Modifier
git add README.md
git commit -m "📝 Ajout du README avec documentation complète"
git push origin main
```
