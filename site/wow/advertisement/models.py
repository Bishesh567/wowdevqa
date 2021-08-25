from django.db import models

# Create your models here.
class database(models.Model):
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    age = models.CharField(max_length = 3)
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 50)
    #gender = models.CharField(max_length = 20)

