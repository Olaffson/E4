import pytest
from django.urls import reverse
from django.test import Client


@pytest.fixture
def client():
    return Client()


def test_home(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert b"AppWeb E4" in response.content
