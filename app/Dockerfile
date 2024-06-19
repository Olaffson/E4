# Utiliser une image de base officielle de Python 3.10
FROM python:3.10-slim

# Définir les variables d'environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY ./appweb /app

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt /app/requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel l'application va écouter
EXPOSE 8000

# Commande pour lancer l'application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "appweb.wsgi:application"]
