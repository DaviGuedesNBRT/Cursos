from django.test import TestCase
from django.urls import reverse, resolve, client

# Create your tests here.


class ReceitaUrlTest(TestCase):
    def test_receitas_home_correta(self):
        homeUrl = reverse("Receitas:Receitas-home")
        self.assertEqual(homeUrl,'/')

    def teste_receita_detail_correta(self):
        detailUrl = reverse("Receitas:Receitas-detail", kwargs={'id': 1})
        self.assertEqual(detailUrl, '/receita/1/')
    
    def teste_receita_nova_correta(self):
        novaUrl = reverse("Receitas:Receitas-nova-receita")
        self.assertEqual(novaUrl, '/nova-receita/')

    def teste_receita_minhas_correta(self):
        minhasUrl = reverse("Receitas:Receitas-minhas-receitas")
        self.assertEqual(minhasUrl, '/minhas-receitas/')

    def teste_receita_favoritas_correta(self):
        favoritasUrl = reverse("Receitas:Receitas-receitas-favoritas")
        self.assertEqual(favoritasUrl, '/receitas-favoritas/')

    def teste_receita_pendentes_correta(self):
        pendentesUrl = reverse("Receitas:Receitas-receitas-pendentes")
        self.assertEqual(pendentesUrl, '/receitas-pendentes/')

    def teste_receita_aprovar_correta(self):
        aprovarUrl = reverse("Receitas:Receitas-aprovar-receita", kwargs={'id': 1})
        self.assertEqual(aprovarUrl, '/aprovar-receita/1/')

    def teste_receita_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)