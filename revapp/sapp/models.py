from django.db import models

# Create your models here.
class Department(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptname=models.CharField(max_length=30)
    def __str__(self):
        return self.deptname

class employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=30)
    salary=models.IntegerField()

    department=models.ForeignKey(Department,null=True,on_delete=models.SET_NULL)


    def __str__(self):
        return self.empname




