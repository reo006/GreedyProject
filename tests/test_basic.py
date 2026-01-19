import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_home_page(client):
    response = client.get(reverse('core:home'))
    assert response.status_code == 200
    assert 'Greedy' in response.content.decode()


@pytest.mark.django_db
def test_login_page(client):
    response = client.get(reverse('accounts:login'))
    assert response.status_code == 200
    assert 'ログイン' in response.content.decode()


@pytest.mark.django_db
def test_signup_page(client):
    response = client.get(reverse('accounts:signup'))
    assert response.status_code == 200
    assert '新規アカウント作成' in response.content.decode()


def test_search_page(client):
    response = client.get(reverse('core:search'))
    assert response.status_code == 200
    assert '商品検索' in response.content.decode()


@pytest.mark.django_db
def test_order_list_requires_login(client):
    response = client.get(reverse('orders:order_list'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_order_creation_flow(client):
    user = User.objects.create_user(username='tester', password='secret')
    client.force_login(user)
    response = client.get(reverse('orders:create_order'))
    assert response.status_code == 200
    assert '注文を作成' in response.content.decode()

