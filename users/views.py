from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from cars.models import Car



def home_view(request):
    return render(request,'base/home.html')

@login_required
def protected_view(request):
    return render(request,'base/page.html')

def signup_view(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            #login the user after the signup
            login(request,user)
            #redirect to the home page
            return redirect('home') 
    else:
        form=CustomUserCreationForm()

    #data=
    return render(request,'users/signup.html',{'form':form})

@login_required
def dashbord_view(request):
    user_cars=Car.objects.filter(owner=request.user)
    data={'user_cars':user_cars}
    return render(request,'users/dashbord.html',data)