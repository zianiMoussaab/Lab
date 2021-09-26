from django import forms
from .models import lab


class CreateNewList(forms.Form):
    full_name = forms.CharField(label="Nom du Laboratoire",max_length=150)
    username = forms.CharField(label="Nom d'Utilisateur",max_length=64)
    password = forms.CharField(label="Mot de Passe",widget=forms.PasswordInput())
    city = forms.CharField(label="Ville",max_length=64)
    region = forms.CharField(label="Region",max_length=64)
    adress = forms.CharField(label="Adresse complete",max_length=200, widget=forms.Textarea(attrs={'rows':2}))
    tel = forms.CharField(label="Numéro de Téléphone 1",min_length=8, max_length=10)
    tel2 = forms.CharField(label="Numéro de Téléphone 2 (optionel)", min_length=8, max_length=10,required=False)
    email = forms.EmailField(label="Email",max_length=120)


class LoginList(forms.Form):
    username = forms.CharField(label="Nom d'Utilisateur",max_length=64)
    password = forms.CharField(label="Mot de Passe",widget=forms.PasswordInput())