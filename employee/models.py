from django.db import models
from django.contrib.auth.models import User

def employee_id_gen():
    last_emp = Employee.objects.all().order_by("id").last()
    if not last_emp:
        return "ABC" + "0001"
    new_emp = int(last_emp.emp_id[-4:]) + 1
    new_emp_id = "ABC" + str(str(new_emp).zfill(4))
    return new_emp_id

class Employee(models.Model):
    Full_name = models.CharField(max_length = 100)
    emp_id = models.CharField(max_length = 10, default = employee_id_gen)
    email_id = models.EmailField()
    # prof_pic = models.FileField(upload_to = "uploads/prof_pics/")

class Address(models.Model):
    emp = models.ForeignKey('Employee', on_delete = models.CASCADE)
    h_no_or_name = models.CharField(max_length = 200)
    add_line_1 = models.CharField(max_length = 1000)
    add_line_2 = models.CharField(max_length = 1000)
    zip_code = models.CharField(max_length = 20)
