from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'galeria/index.html')

def menu(request):
    return HttpResponse('<h1>Menu</h1><p>Liguiça na tarraqueta</p>')

def imagem(request):
    return render(request, 'galeria/imagem.html')

