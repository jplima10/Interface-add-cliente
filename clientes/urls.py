from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('atualiza_clientes/', views.att_cliente, name="atualiza_cliente")
]