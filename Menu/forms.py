from django import forms
from .models import Comida

class ComidaForm(forms.ModelForm):
    class Meta:
        model = Comida
        fields = ['nombre', 'descripcion', 'precio', 'categoria']
        labels = {
            'nombre': 'Nombre de la comida',
            'descripcion': 'Descripción de la comida',
            'precio': 'Precio de la comida',
            'categoria': 'Categoría a la que pertenece la comida',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'EJ: Pollo a la brasa'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'EJ: Pollo a la brasa con papas fritas/arroz/puré'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'EJ: 5000'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }