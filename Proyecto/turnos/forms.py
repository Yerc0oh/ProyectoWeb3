from django import forms
from .models import Disponibilidad

class DisponibilidadForm(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = ['id_doctor', 'dia_semana', 'hora_inicio', 'hora_fin']
        widgets = {
            'hora_inicio': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'hora_fin': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }