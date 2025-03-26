from django.db import models
from django.db.models import Model

# Create your models here.
class student(models.Model):
    student_id=models.AutoField(primary_key=True)
    rollno=models.TextField()
    name=models.TextField()
    department=models.TextField()
    phone=models.TextField()
    city = models.CharField(max_length=100) 

    class meta:
        dp_table="student_detail"
