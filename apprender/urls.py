from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insertar_usuario/', views.insertar, name="insertar_u"),
]