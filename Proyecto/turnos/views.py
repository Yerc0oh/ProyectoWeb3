from django.shortcuts import render, redirect
from .forms import DisponibilidadForm
from .models import Disponibilidad

def crear_disponibilidad(request):
    if request.method == 'POST':
        form = DisponibilidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_disponibilidad')
    else:
        form = DisponibilidadForm()
    return render(request, 'turnos/crear_disponibilidad.html', {'form': form})

def ver_disponibilidad(request):
    disponibilidades = Disponibilidad.objects.all().order_by('id_doctor', 'dia_semana', 'hora_inicio')
    return render(request, 'turnos/ver_disponibilidad.html', {'disponibilidades': disponibilidades})