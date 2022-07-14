from django import forms
from django.forms import ModelForm
from .models import Review

#Crea un form per inserire i dati della recensione, un form alla fine è una classe che poi importo nel html
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('nome' , 'cognome' , 'descrizione' , 'stelle')

        widgets = {
            'nome' : forms.TextInput(attrs={'class':'form-control'}),
            'cognome' : forms.TextInput(attrs={'class':'form-control'}),
            'descrizione' : forms.Textarea(attrs={'class':'form-control'}),
            'stelle' : forms.NumberInput(attrs={'class':'form-control', 'max':'5' , 'min':'1'})
        }

        