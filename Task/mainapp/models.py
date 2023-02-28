from django.db import models

class School(models.Model):
    school_name = models.CharField(max_length= 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.school_name


class Student(models.Model):
    student_name =models.CharField(max_length= 50)
    enrollment = models.IntegerField(unique= True)
    school = models.ForeignKey(School , on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.student_name


# Create your models here.
