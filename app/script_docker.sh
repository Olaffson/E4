# construire le conteneur
docker build -t appweb .

# pour tester le conteneur en local
# docker run -p 8000:8000 appweb

# # pour push le conteneur sur dockerhub
docker tag appweb olaffsen/appweb:latest

docker push olaffsen/appweb:latest
