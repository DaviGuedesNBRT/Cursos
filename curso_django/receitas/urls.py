from django.urls import path
from receitas.views import my_view

urlpatterns = [
    path('', my_view),
]