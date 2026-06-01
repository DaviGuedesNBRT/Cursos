from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .utils.receitas.inject import make_recipe
from receitas.models import tb_receitas, tb_categorias


def register(request):
    return render(request, 'receitas/pages/register.html')

def login(request):
    return render(request, 'receitas/pages/login.html')

def home(request):
    categorias = tb_categorias.objects.all()
    recipe = tb_receitas.objects.all()
    return render(request, 'receitas/pages/index.html', context={
        'receitas': recipe, 'categorias': categorias
    })

def receita(request, id):
    receita = tb_receitas.objects.filter(rec_id=id).first()
    return render(request, 'receitas/pages/receita.html', context={
        'receita': receita
    })

def nova_receita(request):
    return render(request, 'receitas/pages/nova_receita.html')

def minhas_receitas(request):
    return render(request, 'receitas/pages/minhas_receitas.html')

def receitas_favoritas(request):
    return render(request, 'receitas/pages/receitas_favoritas.html')