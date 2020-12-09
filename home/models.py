from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    subject = models.CharField(max_length = 50)
    message = models.TextField(max_length = 255)

class signup(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    phone = models.CharField(max_length = 12)
    password = models.TextField(max_length = 255)