from django.db import models



class Student(models.Model):
    Student_name = models.CharField(max_length = 100)
    Student_roll = models.IntegerField(default=0)
    Student_department = models.CharField(max_length = 100)
    Student_contact = models.CharField(max_length = 200)
    Student_idenntity = models.CharField(max_length= 100)

# Create your models here.
