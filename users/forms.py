from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','email','phone_number','date_of_birth','password1','password2']
        

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name in self.fields:
                self.fields[field_name].help_text = ""  # Removes unwanted messages
                self.fields[field_name].widget.attrs.update({'class': 'form-control'})  # Adds Bootstrap styles