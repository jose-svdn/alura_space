from django.urls import path
from galeria.views import index, menu, imagem

urlpatterns = [
    path('', index, name='index'),
    path('menu', menu),
    path('imagem/', imagem, name='imagem'),

]

