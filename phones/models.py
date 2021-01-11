from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField

# Create your models here.
from accounts.models import UserProfile


class Phone(models.Model):

    brand = models.CharField(blank=False,max_length=15)
    price = models.PositiveIntegerField(blank=False)
    capacity = models.CharField(max_length=15,blank=False)
    picture = models.ImageField(upload_to='phones', blank=False)
    condition = models.CharField(max_length=15,blank=False)
    description = models.TextField()
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.brand + ' ' + self.owner.user.username


