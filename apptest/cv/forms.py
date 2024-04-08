
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput

from .models import UploadedFile

# - Create/Register a user

class CreateUserForm(UserCreationForm):

    username = forms.CharField(help_text=False)

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)


    class Meta:

        model = User
        fields = [
        'username', 
        
        'email', 

        'first_name',

    

        'last_name',
        
        'password1', 
        
        'password2'
 ]


# - Authenticate a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)