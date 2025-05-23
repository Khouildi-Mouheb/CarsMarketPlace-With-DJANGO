from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('users.urls')),


    path('cars/',include('cars.urls')),




    path('rooms/',include('rooms.urls')),
    path('posts/',include('social.urls')),

    
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
