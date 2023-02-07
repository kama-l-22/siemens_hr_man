from django.db import models
from django.utils import timezone
# Create your models here.


#emp_code should be unique for same... 
class qdmin(models.Model):
    Emp_code = models.CharField(max_length=50)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    joined_date = models.DateField(default=timezone.now)
    phone = models.BigIntegerField(null=True,blank=True)


    def __str__(self) -> str:
        return self.first_name+ " "+self.last_name
class manager(models.Model):
    Emp_code = models.CharField(max_length=50)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    joined_date = models.DateField(default=timezone.now)
    phone = models.BigIntegerField(null=True,blank=True)
    
    def __str__(self) -> str:
        return self.first_name+ " "+self.last_name
class employee(models.Model):
    Emp_code = models.CharField(max_length=50)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    employee_score = models.IntegerField(default=0)
    joined_date = models.DateField(default=timezone.now)
    phone = models.BigIntegerField(null=True,blank=True)
    address = models.TextField(max_length=200)
    skills = models.CharField(max_length=100)
    c_w_p = models.CharField(max_length=100,default='company')
    manager = models.ForeignKey(manager,on_delete=models.CASCADE,null=True,
    blank=True)
    def __str__(self) -> str:
        return self.first_name+ " "+self.last_name
class request_employee(models.Model):
    Emp_code = models.CharField(max_length=50)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    employee_score = models.IntegerField(default=0)
    joined_date = models.DateField(default=timezone.now)
    phone = models.BigIntegerField(null=True,blank=True)
    address = models.TextField(max_length=200)
    skills = models.CharField(max_length=100)
    c_w_p = models.CharField(max_length=100,default='company')
    manager = models.CharField(null=True,
    blank=True,max_length=100)
    request_by = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.first_name+ " "+self.last_name



class hr(models.Model):
    Emp_code = models.CharField(max_length=50)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    joined_date = models.DateField(default=timezone.now)
    phone = models.BigIntegerField(null=True,blank=True)
    

    def __str__(self) -> str:
        return self.first_name+ " "+self.last_name


class requestleave(models.Model):
    empidforleave = models.CharField(max_length=100)
    dateofleave = models.DateField(default=timezone.now)
    reasonofleave = models.CharField(max_length=200)
    inperson_charge = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self) -> str:
        return self.empidforleave

class approvedleave(models.Model):
    empidforleave = models.CharField(max_length=100)
    dateofleave = models.CharField(max_length=100)
    reasonofleave = models.CharField(max_length=200)
    approved_by = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.empidforleave

class report(models.Model):
    empid_for_report =models.CharField(max_length=100)
    doucment_overview = models.FileField(upload_to='report_fils')
    submit_date = models.DateField(default=timezone.now)
    compliction_status = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.empid_for_report

class req_hr(models.Model):
    Emp_code = models.CharField(max_length=50)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    joined_date = models.DateField(default=timezone.now)
    phone = models.BigIntegerField(null=True,blank=True)
    req_by = models.CharField(default='own', max_length=100)

    def __str__(self) -> str:
        return self.first_name+ " "+self.last_name
class req_man(models.Model):
    Emp_code = models.CharField(max_length=50)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    joined_date = models.DateField(default=timezone.now)
    phone = models.BigIntegerField(null=True,blank=True)
    req_by = models.CharField(default='own', max_length=100)

    def __str__(self) -> str:
        return self.first_name+ " "+self.last_name

