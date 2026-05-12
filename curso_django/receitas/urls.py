from django.urls import path
from receitas.views import my_view, register

urlpatterns = [
    path('', my_view, name='home'),
    path('register/', register, name='register'),
]