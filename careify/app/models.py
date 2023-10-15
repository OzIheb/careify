from django.db import models

# Create your models here.
#user model

class User(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    
    _counter = -1     #static counter to keep track of number of users
    
    def getcounter():
        User._counter += 1
        return User._counter
    