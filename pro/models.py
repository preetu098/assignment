from django.db import models

# Create your models here.

class AssignmentHelp(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=40)
    location=models.CharField(max_length=50)
    phone_code=models.CharField(max_length=3)
    phone=models.CharField(max_length=13)
    details=models.TextField()
    subject=models.CharField(max_length=225)
    want=models.CharField(max_length=20)
    meeting=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    budget=models.CharField(max_length=60)
    workmode=models.CharField(max_length=30)
    gender=models.CharField(max_length=50)
    language=models.CharField(max_length=60)
    documents=models.FileField()

    