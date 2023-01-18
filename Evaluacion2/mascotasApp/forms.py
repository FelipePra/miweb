from django import forms

from mascotasApp.models import Mascota

class FormMascota(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre','especie']
        nombre = forms.CharField()
        especie = forms.CharField()