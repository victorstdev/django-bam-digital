# atendimentos/forms.py
from django import forms
from .models import Medico, Boletim

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome']

class BoletimForm(forms.ModelForm):
    class Meta:
        model = Boletim
        fields = '__all__'

class AdicionarMedicosCSVForm(forms.Form):
    arquivo_csv = forms.FileField(label="Arquivo", required=True)
