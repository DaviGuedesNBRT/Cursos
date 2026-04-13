from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def my_view(request):
    return render(request, 'receitas/index.html', {'name': 'Davi guedes'})

def contato(request):
    return HttpResponse("Página de contato")
