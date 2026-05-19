from django.urls import path
from receitas import views

urlpatterns = [
    path('', views.home, name='Receitas-home'),
    path('register/', views.register, name='Receitas-register'),
    path('login/', views.login, name='Receitas-login'),
    path('receita/<int:id>/', views.receita, name='Receitas-detail'),
    path('nova-receita/', views.nova_receita, name='Receitas-nova-receita'),
    path('minhas-receitas/', views.minhas_receitas, name='Receitas-minhas-receitas'),
]


