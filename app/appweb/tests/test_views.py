import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_home(client):
    # Créer un utilisateur de test
    user = User.objects.create_user(
        username='testuser',
        password='testpassword'
    )

    # Se connecter avec l'utilisateur de test
    client.login(
        username='testuser',
        password='testpassword'
    )

    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert b"Bonjour, testuser" in response.content
