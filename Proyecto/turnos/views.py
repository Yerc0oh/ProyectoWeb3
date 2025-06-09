from django.shortcuts import render, redirect
from .forms import DisponibilidadForm
from datetime import datetime, timedelta
from .models import Doctor, Disponibilidad, Turno

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

def horarios_disponibles(request, id_doctor, dia):
    doctor = Doctor.objects.get(id_doctor=id_doctor)
    disponibilidad = Disponibilidad.objects.filter(id_doctor=doctor, dia_semana=dia)

    turnos_existentes = Turno.objects.filter(id_doctor=doctor)

    horas_disponibles = []

    for disp in disponibilidad:
        hora = datetime.combine(datetime.today(), disp.hora_inicio)
        fin = datetime.combine(datetime.today(), disp.hora_fin)
        while hora < fin:
            ocupado = turnos_existentes.filter(fecha_hora__time=hora.time(), fecha_hora__week_day=hora.weekday()+1).exists()
            if not ocupado:
                horas_disponibles.append(hora.time())
            hora += timedelta(minutes=30)

    return render(request, 'turnos/horarios_disponibles.html', {
        'doctor': doctor,
        'dia': dia,
        'horas_disponibles': horas_disponibles
    })