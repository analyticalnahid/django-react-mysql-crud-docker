from django.db import models


class Department(models.Model):
    depId = models.AutoField(primary_key=True)
    depName = models.CharField(max_length=10)

    def __str__(self):
        return self.depName
    
class Employee(models.Model):
    empId = models.AutoField(primary_key=True)
    empName = models.CharField(max_length=10)
    depName = models.CharField(max_length=10)
    joiningDate = models.DateField()
    photoName = models.CharField(max_length=500)
    
    def __str__(self):
        return self.empName
    