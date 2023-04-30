from django import forms

class AtividadesForm(forms.Form):
    nome = forms.CharField(max_length=50)
    dia = forms.IntegerField()
    mes = forms.IntegerField()
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()


from core.models import AtividadesModel
from django.forms import ModelForm

class AtividadesModelForm(ModelForm):
    class Meta:
        model = AtividadesModel
        fields = ['nome', 'dia', 'mes']
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()