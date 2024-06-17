#!/bin/bash


# ce fichier permet de supprimer les ressources azure


# Fonction pour afficher un message INFO
print_info() {
    echo -e "\e[32mINFO:\e[0m \e[97m$1\e[0m"
}

# Fonction pour la destruction Terraform
terraform_destroy() {
    cd terraform
    terraform destroy --auto-approve
}

# Appel des fonctions dans l'ordre souhaité
print_info "Destruction des ressources azure..."
terraform_destroy
