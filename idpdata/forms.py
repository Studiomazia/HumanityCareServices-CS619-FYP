from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from idpdata.models import User


class IDPRegistration(forms.ModelForm):
	class Meta:
		model   =   User
		fields  =    ['name','age','city','needs']
        #widgets  =   {'name':forms.TextInput(attrs={'class':'form-control'})}