from django import forms

class HomeForm(forms.Form):
    url = forms.CharField(label='Airbnb URL', max_length=100)
