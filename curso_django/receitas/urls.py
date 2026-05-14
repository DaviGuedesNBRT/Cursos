from django.urls import path
from receitas import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('receita/<int:id>/', views.receita, name='receita'),
    path('nova-receita/', views.nova_receita, name='nova_receita'),
    path('minhas-receitas/', views.minhas_receitas, name='minhas_receitas'),
]


