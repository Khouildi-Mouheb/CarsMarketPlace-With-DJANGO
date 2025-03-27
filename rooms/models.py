from django.db import models
from django.conf import settings


class Room(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    creator=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='created_rooms')
    participants=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='joined_rooms')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name