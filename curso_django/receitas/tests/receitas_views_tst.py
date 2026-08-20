from django.test import TestCase
from django.urls import reverse, resolve
import receitas.views as views
# Create your tests here.


class ViewTest(TestCase):
    def test_receitas_home_view_correta(self):
        view_home = resolve('/')
        self.assertIs(view_home, views.home )

    def test_receitas_detail_view_correta(self):
        view_detail = resolve('/receita/1/')
        self.assertIs(view_detail, views.receita )
        
    def test_receitas_nova_receita_view_correta(self):
        view_nova_receita = resolve('/nova-receita/')
        self.assertIs(view_nova_receita, views.nova_receita )

    def test_receitas_minhas_receitas_view_correta(self):
        view_minhas_receitas = resolve('/minhas-receitas/')
        self.assertIs(view_minhas_receitas, views.minhas_receitas )

    def test_receitas_receitas_favoritas_view_correta(self):
        view_receitas_favoritas = resolve('/receitas-favoritas/')
        self.assertIs(view_receitas_favoritas, views.receitas_favoritas )

    def test_receitas_receitas_pendentes_view_correta(self):
        view_receitas_pendentes = resolve('/receitas-pendentes/')
        self.assertIs(view_receitas_pendentes, views.receitas_pendentes )

    def test_receitas_aprovar_receita_view_correta(self):
        view_aprovar_receita = resolve('/aprovar-receita/1/')
        self.assertIs(view_aprovar_receita, views.aprovar_receita )

    