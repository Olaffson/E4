#!/bin/bash


# ce script permet de creer l environnement virtuel


# Fonction pour afficher un message INFO
print_info() {
    echo -e "\e[32mINFO:\e[0m \e[97m$1\e[0m"
}

chmod +x 02.sh

# Chemin de l'environnement virtuel
ENV_DIR="e4-env"

# Vérifier si l'environnement virtuel existe
if [ ! -d "$ENV_DIR" ]; then
  print_info "Création de l'environnement virtuel..."
  python3 -m venv $ENV_DIR
fi

# Activer l'environnement virtuel
print_info "Activation de l'environnement virtuel..."
source $ENV_DIR/bin/activate

# Installer les dépendances requises depuis requirements.txt
#pip install -r requirements.txt

#chmod +x run_streamlit.sh
