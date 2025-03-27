from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    #override the email field to make it unique
    email=models.EmailField(unique=True)

    #custom fields
    phone_number=models.CharField(max_length=15,blank=True,null=True)
    profile_picture=models.ImageField(upload_to='profile_pics',blank=True,null=True)
    date_of_birth=models.DateField(blank=True,null=True)

    #set the email the primary field for authentication
    USERNAME_FIELD='email'

    #field required when creationg a super user
    REQUIRED_FIELDS=['username']


    def __str__(self):
        return self.username
