#!/bin/bash


# ce script crée la bdd sqlite pour django


# Fonction pour afficher un message INFO
print_info() {
    echo -e "\e[32mINFO:\e[0m \e[97m$1\e[0m"
}

cd appweb

print_info "Création de la bdd sqlite..."
python manage.py migrate

# python manage.py runserver
