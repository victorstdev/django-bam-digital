from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('medicos/', lista_medicos, name='lista_medicos'),
    path('medicos/adicionar', adicionar_medico, name='adicionar_medico'),
    path('medicos/<int:pk>/', detalhes_medico, name='detalhes_medico'),
    path('medicos/editar/<int:pk>/', editar_medico, name='editar_medico'),
    path('medicos/excluir/<int:pk>/', excluir_medico, name='excluir_medico'),
    path('medicos/adicionar_medicos_csv/', adicionar_medicos_csv, name='adicionar_medicos_csv'),
    path('boletins/', lista_boletins, name='lista_boletins'),
    path('boletins/adicionar', adicionar_boletim, name='adicionar_boletim'),
    path('boletins/<int:pk>/', detalhes_boletim, name='detalhes_boletim'),
    path('boletins/editar/<int:pk>/', editar_boletim, name='editar_boletim'),
    path('boletins/excluir/<int:pk>/', excluir_boletim, name='excluir_boletim'),
]