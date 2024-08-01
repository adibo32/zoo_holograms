from django import forms
from .models import Hologram

class HologramForm(forms.ModelForm):
    ausgestorben_seit = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Hologram
        fields = ['name', 'gewicht', 'superkraft', 'ausgestorben_seit']