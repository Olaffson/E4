# Projet E4 - Application Django

Ce projet contient une application Django déployée sur Azure Container Instances (ACI) en utilisant Docker et Terraform.

Le dossier `app` contient plusieurs scripts qui permettent de gérer le projet :
- `script_init` crée et lance l'environnement virtuel.  
- `script_docker` crée le conteneur de l'application django `appweb` et le pousse sur dockerhub.  
- `script_terraform_create` crée les ressources azures nécessaires au projet.  
- `script_terraform_destroy` supprime les ressources azures
