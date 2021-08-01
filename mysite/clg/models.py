from django.db import models
from django.db.models.base import Model

# Create your models here.

class Permission(models.Model):
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=350)
    subject=models.CharField(max_length=250)
    date=models.DateField()
    reason=models.CharField(max_length=250)
    status = models.BooleanField(default=False)

    
    def __str__(self):
        return self.name
    def get_status(self):
        return self.status

class Payment(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

