from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisteration

from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from Home.models import Doctor
from Home.models import Patient
from Home.models import Appoinment




# Create your views here.


def register(request):


    if request.method == 'POST':
        form = UserRegisteration(request.POST)
        if form.is_valid():
            user =form.save()
            if form.cleaned_data.get('is_staff_field') == 'S':
                user.is_staff = True  
            user.save()
            auth_login(request,user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} Your Account has been created')
            return redirect('staff_login')
    else:
        form = UserRegisteration()
    return render (request ,'users/registeration.html' , {'form' : form})





def logout_staff(request):
  
    request.session.flush()
    messages.success(request, "You have been logged out successfully.")
    return redirect('staff_login')



def staff_login_view(request):
    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']
        
      
        user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            if user.is_staff:
                
                auth_login(request, user)
                
                return redirect('staff_dashboard') 
            else:
               auth_login(request, user)
               return redirect('user_dashboard')  
        else:
           
            messages.error(request, 'Invalid username or password.')
    
  
    return render(request, 'users/staff_login.html')


@login_required
def staff_dashboard_view(request):
    if not request.user.is_staff:
        return redirect('user_dashboard')  
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appoinment.objects.all()
    d=0
    p=0
    a=0 
    for i in doctors:
        d+=1

    for i in patient:
        p+=1

    for i in appointment:
        a+=1

    d1 ={'d':d , 'p':p ,'a':a}      

    return render(request, 'users/staff_dashboard.html',d1)

@login_required
def user_dashboard_view(request):
    if request.user.is_staff:
        return redirect('staff_dashboard')  

    specialties = Doctor.objects.values_list('special', flat=True).distinct()
    areas = Doctor.objects.values_list('area', flat=True).distinct()
    doctors = Doctor.objects.all()

   
    if request.method == 'GET':
        search_query = request.GET.get('search', '').strip()  
        special_search = request.GET.get('special', '')       
        area_search = request.GET.get('area', '')             

        if search_query:
            
            search_parts = [part.strip() for part in search_query.split('-')]

           
            if len(search_parts) == 2:
                special_search = search_parts[0]  
                area_search = search_parts[1]     

           
            elif len(search_parts) == 1:
                special_search = search_parts[0]  

     
        if special_search:
            doctors = doctors.filter(special__icontains=special_search)
        if area_search:
            doctors = doctors.filter(area__icontains=area_search)

    context = {
        'specialties': specialties,
        'areas': areas,
        'doctors': doctors,  
    }

    return render(request, 'users/user_dashboard.html', context)
