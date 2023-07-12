from django.db import models

# Create your models here.
class Students(models.Model):
    fio = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=13)
    kurs = models.IntegerField()
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    birthdate = models.DateField()
    is_active = models.BooleanField()
    info = models.TextField()