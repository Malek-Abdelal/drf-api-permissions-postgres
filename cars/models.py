from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Car(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    company = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year_of_production = models.IntegerField()
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.company

