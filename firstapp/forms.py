from django import forms
from .models import book
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class book1(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'
 
# creating a form  
class InputForm(forms.Form): 
   
    first_name = forms.CharField(max_length = 200) 
    last_name = forms.CharField(max_length = 200) 
    roll_number = forms.IntegerField( help_text = "Enter 6 digit roll number") 
    password = forms.CharField(widget = forms.PasswordInput())
   

# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')