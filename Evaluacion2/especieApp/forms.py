from django import forms

from especieApp.models import Especie

class FormEspecie(forms.ModelForm):
    class Meta:
        model = Especie
        fields = ['especie']
        especie = forms.CharField()