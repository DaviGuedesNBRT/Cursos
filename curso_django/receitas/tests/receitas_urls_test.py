from django.test import TestCase
from django.urls import reverse, resolve
import views
# Create your tests here.


class ReceitaUrlTest(TestCase):
    def test_receitas_home_correta(self):
        homeUrl = reverse("Receitas:Receitas-home")
        self.assertEqual(homeUrl,'/')

    def teste_receita_detail_correta(self):
        detailUrl = reverse("Receitas:Receitas-detail", kwargs={'id': 1})
        self.assertEqual(detailUrl, '/receita/1/')
