import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User


# @pytest.mark.django_db
# def test_home(client):
#     # Créer un utilisateur de test
#     user = User.objects.create_user(
#         username='testuser',
#         password='testpassword'
#     )

#     # Se connecter avec l'utilisateur de test
#     client.login(
#         username='testuser',
#         password='testpassword'
#     )

#     url = reverse('home')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert b"Bonjour, testuser" in response.content


@pytest.mark.django_db
def test_home_authenticated(client):
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

@pytest.mark.django_db
def test_home_unauthenticated(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))

@pytest.mark.django_db
def test_404_page(client):
    response = client.get('/nonexistent-page/')
    assert response.status_code == 404
    assert b"404 - Page Not Found" in response.content
