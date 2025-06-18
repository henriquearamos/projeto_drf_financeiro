from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from transacoes.models import Fonte  # ajuste o import conforme seu projeto

class TestTransacaoAuth(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste-user', password='teste123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Cria uma fonte válida para usar no teste
        self.fonte = Fonte.objects.create(nome_fonte='Salário')

    def test_criar_transacao_autenticado(self):
        url = reverse('transacao-list')
        data = {
            "tipo_entrada": "credito",
            "fonte_id": self.fonte.id,
            "data": "2025-06-07",
            "valor": "80.29"
        }
        response = self.client.post(url, data, format='json')
        print(response.data)  # ajuda a debugar se ainda falhar
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


