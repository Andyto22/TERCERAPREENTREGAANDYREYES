from django import forms
from .models import Curso

class ItemForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion']
