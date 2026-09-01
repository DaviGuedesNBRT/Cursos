from django.test import TestCase
from django.urls import reverse, resolve
import receitas.views as views


class ViewTest(TestCase):
    def test_receitas_home_view_correta(self):
        view_home = resolve('/')
        self.assertIs(view_home.func, views.home)

    def test_receitas_detail_view_correta(self):
        view_detail = resolve('/receita/1/')
        self.assertIs(view_detail.func, views.receita)

    def test_receitas_nova_receita_view_correta(self):
        view_nova_receita = resolve('/nova-receita/')
        self.assertIs(view_nova_receita.func, views.nova_receita)

    def test_receitas_minhas_receitas_view_correta(self):
        view_minhas_receitas = resolve('/minhas-receitas/')
        self.assertIs(view_minhas_receitas.func, views.minhas_receitas)

    def test_receitas_receitas_favoritas_view_correta(self):
        view_receitas_favoritas = resolve('/receitas-favoritas/')
        self.assertIs(view_receitas_favoritas.func, views.receitas_favoritas)

    def test_receitas_receitas_pendentes_view_correta(self):
        view_receitas_pendentes = resolve('/receitas-pendentes/')
        self.assertIs(view_receitas_pendentes.func, views.receitas_pendentes)

    def test_receitas_aprovar_receita_view_correta(self):
        view_aprovar_receita = resolve('/aprovar-receita/1/')
        self.assertIs(view_aprovar_receita.func, views.aprovar_receita)


class ReceitasViewsStatusCodeTest(TestCase):
    def test_receitas_home_status_code_200(self):
        response = self.client.get(reverse('Receitas:Receitas-home'))
        self.assertEqual(response.status_code, 200)

    def test_receitas_register_status_code_200(self):
        response = self.client.get(reverse('Receitas:Receitas-register'))
        self.assertEqual(response.status_code, 200)

    def test_receitas_login_status_code_200(self):
        response = self.client.get(reverse('Receitas:Receitas-login'))
        self.assertEqual(response.status_code, 200)

    def test_receitas_detail_status_code_200(self):
        response = self.client.get(reverse('Receitas:Receitas-detail', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_receitas_nova_receita_status_code_200(self):
        response = self.client.get(reverse('Receitas:Receitas-nova-receita'))
        self.assertEqual(response.status_code, 200)

    def test_receitas_minhas_receitas_status_code_200(self):
        response = self.client.get(reverse('Receitas:Receitas-minhas-receitas'))
        self.assertEqual(response.status_code, 200)

    def test_receitas_receitas_favoritas_status_code_200(self):
        response = self.client.get(reverse('Receitas:Receitas-receitas-favoritas'))
        self.assertEqual(response.status_code, 200)

    def test_receitas_receitas_pendentes_status_code_200(self):
        response = self.client.get(reverse('Receitas:Receitas-receitas-pendentes'))
        self.assertEqual(response.status_code, 200)

    def test_receitas_aprovar_receita_status_code_200(self):
        response = self.client.get(reverse('Receitas:Receitas-aprovar-receita', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)
