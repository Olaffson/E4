#!/bin/bash

# <module_path> est le chemin relatif vers le dossier qui contient le module avec wsgi.py
# <module> est le nom du module qui contient wsgi.py

# Définir le chemin vers le module et le module lui-même
MODULE_PATH="appweb"
MODULE="appweb"

# Lancer Gunicorn avec les paramètres appropriés
exec gunicorn --bind=0.0.0.0 --timeout 600 --workers=4 --chdir $MODULE_PATH $MODULE.wsgi
