from django import forms


class UserCreate(forms.Form):
    your_name = forms.CharField(label='username', max_length=100)
