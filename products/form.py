from django import forms 
from .models import Product 

class CreateForm(forms.ModelForm):
    class Meta :
        model  = Product
        fields  = ['name','prix','quantity','prixAchat','margeBeneficiere','TVA',]
        
