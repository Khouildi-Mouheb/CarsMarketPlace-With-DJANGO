from django.db import models
from django.conf import settings

class Car(models.Model):
    #choices for car types
    CAR_TYPE_CHOICES=[
        ('mechanical','Mechanical'),
        ('hybrid','Hybrid'),
        ('electric','Electric'),
    ]
    #fields
    #link the owner who posted the car
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #the model of the car
    model=models.CharField(max_length=50)
    #the brand of the car
    brand=models.CharField(max_length=50)
    #description
    description=models.TextField()
    #the type of the car
    type=models.CharField(max_length=20,choices=CAR_TYPE_CHOICES)
    #price of the car
    price=models.DecimalField(max_digits=10,decimal_places=2)
    #the location of the car
    location=models.CharField(max_length=20,blank=True,null=True)
    #image
    image=models.ImageField(upload_to='car_images/',blank=True,null=True)
    #when the car was listed in the shop
    created_at=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.model 
    


class Wishlist(models.Model):
    #link to the user who owns the wishlist
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #link to the car
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    add_on=models.DateTimeField(auto_now_add=True)


    class Meta:
        #ensure a car can be added once
        unique_together=('user','car')

    def __str__(self):
        return f"{self.user.username}-{self.car.brand}"
