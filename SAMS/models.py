from django.core.exceptions import ValidationError
from django.db import models
from account.models import Account


# Create your models here.


class Student(models.Model):
    email = models.ForeignKey(Account,
                              to_field='email', db_column='email', on_delete=models.CASCADE)
    Student_Name = models.CharField(max_length=50)
    Student_ID = models.CharField(max_length=10, unique=True, primary_key=True)
    PrepYear = models.BooleanField(default=False, unique=True)

    def __str__(self):
        return self.Student_Name


class Professor(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    email = models.ForeignKey(Account, to_field='email', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Prepmaterials(models.Model):
    material = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.material


class PrepYear(models.Model):
    course_name = models.ForeignKey(Prepmaterials, on_delete=models.CASCADE)
