from django import forms
from django.utils import timezone
from django.core import validators
from django.core.exceptions import ValidationError
from accouts.models import profile,UserprofileInfo
from django.contrib.auth.models import User



class authform(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField(max_length=32,widget=forms.PasswordInput)
    First_name = forms.CharField()
    Last_name = forms.CharField()
    Email_address= forms.EmailField(validators=[validators.EmailValidator()])
    Varify_Email_address = forms.EmailField(label='Enter A Email Again',validators=[validators.EmailValidator()])
    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput)
    # Date_joined=forms.DateTimeField(default=timezone.now())
    
    # def clean_botcatcher(self):
    #     botcatch = self.cleaned_data['botcatcher']
    #     if(len(botcatch) > 0):
    #         raise forms.ValidationError("GotchA Bot")
    #     return botcatch
    
    def clean_Password(self):
        pwd = self.cleaned_data['Password']
        if(len(pwd) < 6 or len(pwd) > 12):
            raise forms.ValidationError("Password must be 6 or 12")
        return pwd
    
    def clean(self):
        
        # following code is work
        all_data = super().clean()
        email = all_data.get('Email_address')
        vmail = all_data.get('Varify_Email_address')
        
        # following code is also work
        # email = self.cleaned_data.get('Email_address')
        # vmail = self.cleaned_data.get('Varify_Email_address')

        if email != vmail:
            raise forms.ValidationError("Both Email Address must be Match")
        
class profile1(forms.ModelForm):
    class Meta:
        model = profile
        fields = '__all__'
        
class userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username','email','password')   
        
class profileinfo(forms.ModelForm):
    class Meta:
        model = UserprofileInfo
        fields = ('portfolio_site','profile_pic')
             
    