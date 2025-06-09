from django.urls import path
from . import views

urlpatterns = [
    path('crear_disponibilidad/', views.crear_disponibilidad, name='crear_disponibilidad'),
    path('ver_disponibilidad/', views.ver_disponibilidad, name='ver_disponibilidad'),
]
