
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_form

urlpatterns = [
    path('',views.home,name='home'),

    
    path('login/',auth_form.LoginView.as_view(template_name='login.html'),name='login'),
    path('register/',views.register,name='register'),
    
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout_view,name='logout'),
    path('contact/', views.contact, name='contact'),
    

    
  
    
    
    
    
    
  
    

    
    
]