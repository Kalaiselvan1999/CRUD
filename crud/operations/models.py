from django.db import models

# Create your models here.

class Department(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    department_name = models.CharField(max_length=100)



class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)