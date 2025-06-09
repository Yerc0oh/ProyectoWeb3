
from django.shortcuts import render
from .models import Doctor
from .models import Paciente
from django.shortcuts import render, redirect
from .forms import DoctorForm, PacienteForm

def lista_doctores(request):
    doctores = Doctor.objects.select_related('id_especialidad').all()
    return render(request, 'doctor_list.html', {'doctores': doctores})


def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'paciente_list.html', {'pacientes': pacientes})


def registrar_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_doctores')  # o alguna otra vista
    else:
        form = DoctorForm()
    return render(request, 'doctor_form.html', {'form': form})

def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_paciente')  # o alguna otra vista
    else:
        form = PacienteForm()
    return render(request, 'paciente_form.html', {'form': form})