#!/bin/bash


# ce script crée les ressources azure nécessaires pour le projet


# Fonction pour afficher un message INFO
print_info() {
    echo -e "\e[32mINFO:\e[0m \e[97m$1\e[0m"
}

# Fonction pour l'initialisation Terraform
terraform_create() {
    cd terraform
    terraform init
    terraform plan
    terraform apply --auto-approve
}

# Appel des fonctions
print_info "Création des ressources azure..."
terraform_create