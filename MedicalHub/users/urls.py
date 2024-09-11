from django.urls import  path
from .views import logout_staff


from . import views

urlpatterns = [  
   path('logout/',views.logout_staff, name='LogoutPage'),
   path('staff_login/', views.staff_login_view, name='staff_login'),
   path('user_dashboard/', views.user_dashboard_view, name='user_dashboard'),
   path('', views.register , name='RegisterPage'),
   path('staff_dashboard/', views.staff_dashboard_view, name='staff_dashboard'),  # Dashboard URL
]
