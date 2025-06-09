from django.urls import path
from . import views

urlpatterns = [
    path('crear_disponibilidad/', views.crear_disponibilidad, name='crear_disponibilidad'),
    path('ver_disponibilidad/', views.ver_disponibilidad, name='ver_disponibilidad'),
    path('horarios_disponibles/<int:id_doctor>/<str:dia>/', views.horarios_disponibles, name='horarios_disponibles'),
]
