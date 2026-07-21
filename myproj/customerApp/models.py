from django.db import models

# Create your models here.
class Customer(models.Model):
    roll=models.IntegerField(unique=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=15)
    image=models.ImageField(upload_to='students/', blank=True)

    def __str__(self):
        return self.name
