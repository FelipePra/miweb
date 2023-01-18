from django import forms
from personaApp.models import Marca
from personaApp.models import Categoria
from personaApp.models import Producto

class FormMarca(forms.ModelForm):
    class Meta:
        model= Marca
        fields = ['nombre']
        nombre = forms.CharField()

class FormCategoria(forms.ModelForm):
    class Meta:
        model= Categoria
        fields = ['nombre']
        nombre = forms.CharField()        

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        #fields = '__all__'
        fields= ['nombre','precio','stock','marca','categoria','descripcion']
        widgets = {
            'nombre': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'precio': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'stock': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'marca': forms.widgets.Select(attrs={'class':'form-control'}),
            'categoria': forms.widgets.Select(attrs={'class':'form-control'}),
            'descripcion': forms.widgets.Textarea(attrs={'class':'form-control','rows':2})
        }


class FormFiltroProduto(forms.Form):
    marcas = forms.ModelChoiceField(queryset=Marca.objects.all(),
     required=False,
     empty_label='Todas las Marcas',
     widget=forms.Select(attrs={'class': 'form-select'}))
    categorias = forms.ModelChoiceField(queryset=Categoria.objects.all(),
     required=False,
     empty_label='Todas las Categorias',
     widget=forms.Select(attrs={'class': 'form-select'}))
       
         