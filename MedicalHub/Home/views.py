from django.shortcuts import render,redirect , get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import user_passes_test
from .models import Doctor
from .models import Patient
from .models import Appoinment
from django.contrib import messages


# Create your views here.


def home(request):
    doctors = Doctor.objects.all()
    specialties = Doctor.objects.values_list('special', flat=True).distinct()

    

    context = {
        'doctors': doctors,'specialties': specialties,
    }
    return render(request, 'Home/home.html',context)

def about(request):
   
     return render(request, 'Home/about.html')

def contact(request):
   
     return render(request, 'Home/contact.html')

def View_Doctor(request):
     if not request.user.is_staff:
          return redirect('user_dashboard')
     doc =Doctor.objects.all()
     d = {'doc' : doc}
     return render(request,'Home/view_doctor.html',d)

def Delete_Doctor(request,pid):
     if not request.user.is_staff:
          return redirect('user_dashboard')
     doctor =Doctor.objects.get(id=pid)
     doctor.delete()
     
     return redirect('view_doctor')


def Add_Doctor(request):
    if not request.user.is_staff:
          return redirect('user_dashboard')
    error =""
    if request.method == 'POST':
     
        name = request.POST['name']
        mobile = request.POST['mobile']
        special = request.POST['special']
        area = request.POST['area']
       
        try:
             Doctor.objects.create(Name=name, mobile=mobile , special=special , area=area)
             error= 'no'

        except:
             error='yes'
    d={'error':error}   


    if error == "no":
      messages.success(request, "Record save successfully.")   
      return redirect('view_doctor')
    
    elif error == "yes":
       messages.error(request, "please try again.")   

    return render(request, 'Home/add_doctor.html',d)



def View_Patient(request):
     if not request.user.is_staff:
          return redirect('user_dashboard')
     doc =Patient.objects.all()
     d = {'doc' : doc}
     return render(request,'Home/view_patient.html',d)

def Delete_Patient(request,pid):
     if not request.user.is_staff:
          return redirect('user_dashboard')
     patient =Patient.objects.get(id=pid)
     patient.delete()
     
     return redirect('view_patient')


def Add_Patient(request):
    if not request.user.is_staff:
          return redirect('user_dashboard')
    error =""
    if request.method == 'POST':
        
        name = request.POST['name']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        address = request.POST['address']
       
        try:
             Patient.objects.create(name=name,gender=gender, mobile=mobile ,address=address)
             error= 'no'

        except:
             error='yes'
    d={'error':error}   


    if error == "no":
      messages.success(request, "Record save successfully.")   
      return redirect('view_patient')
    
    elif error == "yes":
       messages.error(request, "please try again.")   

    return render(request, 'Home/add_patient.html',d)



def View_Appointment(request):
     if not request.user.is_staff:
          return redirect('user_dashboard')
     doc =Appoinment.objects.all()
     d = {'doc' : doc}
     return render(request,'Home/view_appointment.html',d)

def Delete_Appointment(request,pid):
     if not request.user.is_staff:
          return redirect('user_dashboard')
     appointment =Appoinment.objects.get(id=pid)
     appointment.delete()
     
     return redirect('view_appointment')


def Add_Appointment(request):
    if not request.user.is_staff:
          return redirect('user_dashboard')
    error =""
    doctor1 =Doctor.objects.all()
    patient1 =Patient.objects.all()
    if request.method == 'POST':
        
        doctor = request.POST['doctor']
        patient = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']
        doctor2=Doctor.objects.filter(Name=doctor).first()
        patient2=Patient.objects.filter(name=patient).first()
       
        try:
             Appoinment.objects.create(doctor=doctor2,patient=patient2, date=date ,time=time)
             error= 'no'

        except:
             error='yes'
    d={'doctor':doctor1 ,'patient':patient1 ,'error':error }   


    if error == "no":
      messages.success(request, "Record save successfully.")   
      return redirect('view_appointment')
    
    elif error == "yes":
       messages.error(request, "please try again.")   

    return render(request, 'Home/add_appointment.html',d)


def doctor_detail_view(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    context = {
        'doctor': doctor
    }
    return render(request, 'Home/doctor_detail.html', context)



def BookAppointmentView(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    current_user = request.user
    if not current_user.is_authenticated:
        return redirect('staff_login')  

    if request.method == 'POST':
        patient_name = current_user.username
        date = request.POST['date']
        time = request.POST['time']

        try:
            patient = Patient.objects.filter(name=patient_name).first()
            if not patient:
                patient = Patient.objects.create(name=patient_name)  
            Appoinment.objects.create(doctor=doctor, patient=patient, date=date, time=time)
            messages.success(request, "Appointment booked successfully.")
            return redirect('view_my_appointment')
        except Exception as e:
            messages.error(request, f"Error booking appointment: {e}")

    context = {
        'doctor': doctor,
        'patient_name': current_user.username
    }
    return render(request, 'Home/add_appointment.html', context)



def ViewAppointmentsView(request):
    if not request.user.is_authenticated:
        return redirect('staff_login')  

    current_user = request.user
    patient = Patient.objects.filter(name=current_user.username).first()
    if patient:
        appointments = Appoinment.objects.filter(patient=patient)
    else:
        appointments = []

    context = {
        'appointments': appointments
    }
    return render(request, 'Home/view_my_appointment.html', context)
