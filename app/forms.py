from django import forms
from .models import Adotado

class AdotadoForm(forms.ModelForm):
    class Meta:
        model = Adotado
        fields = [
            'nome', 'idade', 'sexo', 'data_nasc',
            'situacao', 'necessidades_especiais', 'foto'
        ]
        widgets = {
            'data_nasc': forms.DateInput(attrs={'type': 'date'}),
        }
