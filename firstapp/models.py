from django.db import models
# from django.contrib.auth.models import AbstractUser
# Create your models here.

class student(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length = 50)
    semail = models.EmailField(max_length=254)
    
class book(models.Model):
    bname = models.CharField(max_length = 50)
    b_pic = models.ImageField(upload_to='media/image')
    price = models.IntegerField()
    
class register(models.Model):    
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)
    uname = models.CharField(max_length = 50)
    password = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zip = models.CharField(max_length = 50)
    
    def snippet(self):
        return self.password[:3] + '...'
# class CustomUser(AbstractUser):
#     pass
#     # add additional fields in here

#     def __str__(self):
#         return self.username