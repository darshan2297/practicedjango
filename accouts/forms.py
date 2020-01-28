from django import forms
from django.utils import timezone

class authform(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField(max_length=32,widget=forms.PasswordInput)
    First_name = forms.CharField()
    Last_name = forms.CharField()
    Email_address=forms.EmailField()
    # Date_joined=forms.DateTimeField(default=timezone.now())