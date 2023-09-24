from django import forms
from .models import Curso, Estudiante

class cursosForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre','camada']


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']