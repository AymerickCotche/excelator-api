necessite une base de données postgresql de version 14 ou plus

Copier le fichier .env.example et remplacé par .env

Modifier les variables d'environnement

Créer un venv a la racine : "python -m venv venv"

Activer le venv "source venv/bin/activate"
Installer les dépendances : "pip install -r requirements.txt"

faire les migrations: "python manage.py makemigrations"
Migrer les données: "python manage.py migrate"
lancer le serveur : "python manage.py runserver"