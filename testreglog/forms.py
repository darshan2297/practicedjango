from django import forms
from django.contrib.auth.models import User
from testreglog.models import user_reg


class user_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password','first_name','last_name')
        
class reg_form(forms.ModelForm):
    # mobno = forms.IntegerField(widget=forms.TextInput())
    class Meta:
        model = user_reg
        fields = ['mobno']