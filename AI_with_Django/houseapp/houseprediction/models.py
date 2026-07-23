from django.db import models

# Create your models here.
class House(models.Model):
    area = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    age = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.area} sqft, {self.bedrooms} bedrooms, {self.bathrooms} bathrooms, {self.age} years old, Price: ${self.price}'    