from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novo/', views.bliss_create, name='bliss_create'),
    path('editar/<int:pk>/', views.bliss_update, name='bliss_update'),
    path('excluir/<int:pk>/', views.bliss_delete, name='bliss_delete'),
    path('importar/', views.bliss_import, name='bliss_import'),
    path('relatorio/', views.bliss_report, name='bliss_report'),
    path('relatorio/pdf/', views.bliss_pdf_report, name='bliss_pdf_report'),
    path('resumo/', views.bliss_summary, name='bliss_summary'),
    path('atualizar-situacoes/', views.atualizar_situacoes, name='atualizar_situacoes'),
]
