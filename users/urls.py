from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('dashbord/',views.dashbord_view,name='dashbord'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('signup/',views.signup_view,name='signup'),  
    path('protected_page/',views.protected_view,name='protected'),  
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
