from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','email','phone_number','date_of_birth','password1','password2']
        