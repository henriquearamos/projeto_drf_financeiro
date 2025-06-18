import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from transacoes.models import Fonte

@pytest.mark.django_db
def test_criar_transacao_autenticado():
    user = User.objects.create_user(username='teste-user', password='teste123')
    fonte = Fonte.objects.create(nome_fonte='Salário')

    client = APIClient()
    client.force_authenticate(user=user)

    data = {
        "tipo_entrada": "desconto",
        "fonte_id": fonte.id,
        "data": "2025-06-07",
        "valor": "80.29"
    }

    response = client.post('/api/v1/transacoes/', data, format='json')
    assert response.status_code == 201