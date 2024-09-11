
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views
from django.contrib.auth.views import LogoutView
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('users.urls')),
    path('', include('Home.urls')),
]
#+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) 
