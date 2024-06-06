
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import forms
from django import forms
from django import forms
from django import forms
from django.core.exceptions import ValidationError
import re



def validate_alpha(value):
    if not re.match("^[a-zA-Z]*$", value):
        raise ValidationError('Name can only contain alphabets.')




class newReg(UserCreationForm):
  
    class Meta():
        model = User
        fields = ['username','email','password1','password2']
        
        
# class BioDataForm(forms.ModelForm):
#     class Meta:
#         model = BioData
#         fields = ['name', 'email', 'phone_number', 'message']



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,validators=[validate_alpha])
    email = forms.EmailField()
    contact = forms.IntegerField()
    
    message = forms.CharField(widget=forms.Textarea)

        
        
        


