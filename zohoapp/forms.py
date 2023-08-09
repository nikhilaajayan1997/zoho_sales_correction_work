# forms.py
from django import forms
from django.forms import TextInput,EmailInput

class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Name','style': 'width: 50%;','class':'text-dark'}))
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget = forms.Textarea )