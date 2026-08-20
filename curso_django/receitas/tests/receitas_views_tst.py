from django.test import TestCase
from django.urls import reverse, resolve
import views
# Create your tests here.


class ViewTest(TestCase):
    def test_receitas_home_view_correta(self):
        view_home = resolve('/')
        self.assertIs(view_home, views.home )

