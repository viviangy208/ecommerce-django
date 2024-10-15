from django import forms
from .models import Account

class RegistrationForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Ingresar Password',
        'class': 'form-control',
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirmar Password',
        'class': 'form-control',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForms, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']= 'Ingresar nombre'
        self.fields['last_name'].widget.attrs['placeholder']= 'Ingresar apellido'
        self.fields['phone_number'].widget.attrs['placeholder']= 'Ingresar telefono'
        self.fields['email'].widget.attrs['placeholder']= 'Ingresar e-mail'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'