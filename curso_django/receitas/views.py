from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    return render(request, 'receitas/pages/register.html')

def login(request):
    return render(request, 'receitas/pages/login.html')

def home(request):
    return render(request, 'receitas/pages/index.html')

def receita(request, id):
    return render(request, 'receitas/pages/receita.html', context={
        'id': id
    })

