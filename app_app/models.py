from django.db import models

class EmployeeModel(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    emp_type = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name