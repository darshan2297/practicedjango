from django import forms
from django.utils import timezone
from django.core import validators
from django.core.exceptions import ValidationError

class authform(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField(max_length=32,widget=forms.PasswordInput)
    First_name = forms.CharField()
    Last_name = forms.CharField()
    Email_address=forms.EmailField()
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput)
    # Date_joined=forms.DateTimeField(default=timezone.now())
    
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        
        if(len(botcatcher) > 0):
            raise forms.ValidationError("GotchA Bot")
            return botcatcher
            
           
        