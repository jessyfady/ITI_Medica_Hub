from django.urls import  path
from . import views

urlpatterns = [
    path('', views.home , name='Home'),
    path('about/', views.about , name='About'),
    path('contact/', views.contact , name='Contact'),
    path('view_doctor/', views.View_Doctor , name='view_doctor'),
    path('delete_doctor(?P<int:pid>)/', views.Delete_Doctor , name='delete_doctor'),
    path('add_doctor/', views.Add_Doctor , name='add_doctor'),
    path('view_patient/', views.View_Patient , name='view_patient'),
    path('delete_patient(?P<int:pid>)/', views.Delete_Patient, name='delete_patient'),
    path('add_patient/', views.Add_Patient , name='add_patient'),
    path('view_appointment/', views.View_Appointment , name='view_appointment'),
    path('delete_appointment(?P<int:pid>)/', views.Delete_Appointment, name='delete_appointment'),
    path('add_appointment/', views.Add_Appointment, name='add_appointment'),
    path('doctor/<int:id>/',views.doctor_detail_view, name='doctor_detail'),
    path('book_appointment/<int:doctor_id>/', views.BookAppointmentView, name='book_appointment'),
      path('view_my_appointment/', views.ViewAppointmentsView, name='view_my_appointment'),
]