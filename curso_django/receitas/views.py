from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .utils.receitas.inject import make_recipe


def register(request):
    return render(request, 'receitas/pages/register.html')

def login(request):
    return render(request, 'receitas/pages/login.html')

def home(request):
    return render(request, 'receitas/pages/index.html', context={
        'receitas': [make_recipe() for _ in range(10)]
    })

def receita(request, id):
    return render(request, 'receitas/pages/receita.html', context={
        'id': id
    })

def nova_receita(request):
    return render(request, 'receitas/pages/nova_receita.html')


def minhas_receitas(request):
    return render(request, 'receitas/pages/minhas_receitas.html')