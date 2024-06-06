from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import forms
from .forms import *
from django.contrib  import messages
from django.contrib.auth import logout


from django.core.mail import send_mail

from django.conf import settings
from .forms import ContactForm







# Create your views here.

def home(request):
    return render(request,'home.html')


def register(request):

    
    form = newReg(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'your account has been created you can log in now')
        return redirect('login')
    
    return render(request,'register.html',{'form':form})


def logout_view(request):
    logout(request)
    messages.success(request,'Account has bee logged out')
    return redirect('login')
    
    
    
def profile(request):
    return render(request,'profile.html')



# def submit_biodata(request):

#     if request.method == 'POST':

#         form = BioDataForm(request.POST)

#         if form.is_valid():

#             biodata = form.save()

#             # Send email

#             subject = 'New Bio Data Submission'

#             message = f"""

#             Name: {biodata.name}

       

         

#             Email: {biodata.email}

#             Phone Number: {biodata.phone_number}

#             Message: {biodata.message}

#             """

#             recipient = 'naseer.work05@gmail.com'

#             send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient],fail_silently=False)

#             return redirect('profile')

#     else:

#         form = BioDataForm()

#     return render(request, 'contact.html', {'form': form})
        
        
        
def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            message = form.cleaned_data['message']

            subject = 'Task11'
            message = f'Name: {name}\nEmail: {email}\nContact Number: {contact}\nMessage: {message}'
            sender_email = settings.EMAIL_HOST_USER
            recipient_list = [settings.DEFAULT_FROM_EMAIL]

            send_mail(subject, message, sender_email, recipient_list)
            return redirect('profile')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})







