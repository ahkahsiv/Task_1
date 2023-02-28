from django.shortcuts import render
from . models import Student, School
from .serializers import SchoolSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework import viewsets


# for normal Crud operations
def home(request):
    school_data = School.objects.all()
    student_data = Student.objects.all()
    return render(request, "home.html",{'student_data':student_data, 'school_data':school_data})

def update(request):
    id= request.POST['id']
    student_obj = Student.objects.get(id =id)
    student_obj.student_name = request.POST['student_name']
    school_name = request.POST['school_name']
    student_obj.school = School.objects.get( id = school_name)
    student_obj.enrollment = request.POST['enrollment']
    student_obj.save()
    school_data = School.objects.all()
    student_data = Student.objects.all()
    return render(request, "home.html",{'student_data':student_data, 'school_data':school_data})

def add(request):
    school_data =School.objects.all()
    return render(request, 'add_student.html',{'school_data':school_data})

def delete_student(request, id):
    Student.objects.get(id =id ).delete()
    school_data = School.objects.all()
    student_data = Student.objects.all()
    return render(request, "home.html",{'student_data':student_data, 'school_data':school_data})

def add_student(request):
    student_name = request.POST['student_name']
    enrollment = request.POST['enrollment']
    school = request.POST['school']
    school = School.objects.get( id = school)
    Student.objects.create(
        student_name = student_name,
        enrollment= enrollment,
        school = school,
    )
    school_data = School.objects.all()
    student_data = Student.objects.all()
    return render(request, "home.html",{'student_data':student_data, 'school_data':school_data})


# For making API's
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



# Create your views here.
