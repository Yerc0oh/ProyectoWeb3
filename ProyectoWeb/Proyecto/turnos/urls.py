from django.urls import path
from . import views  # Asegúrate de que esto esté

urlpatterns = [
    path('doctores/', views.lista_doctores, name='lista_doctores'),
    path('registrar-doctor/', views.registrar_doctor, name='registrar_doctor'),
    path('registrar-paciente/', views.registrar_paciente, name='registrar_paciente'),
    path('pacientes/', views.paciente_list, name='paciente_list'),


]
