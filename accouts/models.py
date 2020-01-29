from django.db import models

# Create your models here.
class topic(models.Model):
    topic = models.CharField(max_length=120,unique=True)
    
    def __str__(self):
        return self.topic

class webpage(models.Model):
    topic = models.ForeignKey(topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=120,unique=True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name
    
class access(models.Model):
    name = models.ForeignKey(webpage,on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return str(self.date)
    

class user(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length= 150)
    email = models.EmailField(max_length=150,unique=True)
    
    def __str__(self):
        return self.fname
    
class profile(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    email = models.EmailField(max_length=150,unique=True)
    
    def __str__(self):
        return self.fname