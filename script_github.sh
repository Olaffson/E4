# Exécuter autopep8 
# cd app
# autopep8 --in-place --recursive --aggressive --aggressive appweb/

# Envoyer sur git
git add .
git commit -m "Add CI workflow for pycodestyle, pytest, and coverage"
git push origin main