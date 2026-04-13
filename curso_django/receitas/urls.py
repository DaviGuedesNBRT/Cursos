from django.urls import path
from receitas.views import my_view, contato

urlpatterns = [
    path('', my_view),
    path('contato/', contato),
]