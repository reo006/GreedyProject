import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_home_page(client):
    response = client.get(reverse('core:home'))
    assert response.status_code == 200
    assert 'Welcome to Food Delivery App' in response.content.decode()

@pytest.mark.django_db
def test_login_page(client):
    response = client.get(reverse('accounts:login'))
    assert response.status_code == 200
    assert 'Login' in response.content.decode()

@pytest.mark.django_db
def test_signup_page(client):
    response = client.get(reverse('accounts:signup'))
    assert response.status_code == 200
    assert 'Sign Up' in response.content.decode()

@pytest.mark.django_db
def test_profile_edit_page(client):
    response = client.get(reverse('accounts:profile_edit'))
    assert response.status_code == 200
    assert 'Edit Profile' in response.content.decode()

@pytest.mark.django_db
def test_search_page(client):
    response = client.get(reverse('restaurants:search'))
    assert response.status_code == 200
    assert 'Search for Restaurants' in response.content.decode()

@pytest.mark.django_db
def test_order_confirmation_page(client):
    response = client.get(reverse('orders:confirm'))
    assert response.status_code == 200
    assert 'Order Confirmation' in response.content.decode()