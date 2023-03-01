from django.shortcuts import render
from . models import Student, School
from django.db.models import Q
from .serializers import SchoolSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework import viewsets


# for normal Crud operations
def index(request):
    school_data = School.objects.all()
    student_data = Student.objects.all()
    return render(request, "index.html",{'student_data':student_data, 'school_data':school_data})

def update_page(request):
    id = request.GET['id']
    data = Student.objects.get( id = id )
    school_data = School.objects.all()
    return render (request, "update_student.html",{'data':data,'school_data':school_data})

def update(request):
    student_obj = Student()
    student_obj.id = request.POST['id']
    student_obj.student_name = request.POST['student_name']
    student_obj.enrollment = request.POST['enrollment']
    school = request.POST['school']
    student_obj.school = School.objects.get( id = school)
    student_obj.save()
    school_data = School.objects.all()
    student_data = Student.objects.all()
    return render(request, "index.html",{'student_data':student_data, 'school_data':school_data})


def delete_student(request):
    id = request.GET['id']
    Student.objects.get(id =id ).delete()
    school_data = School.objects.all()
    student_data = Student.objects.all()
    return render(request, "index.html",{'student_data':student_data, 'school_data':school_data})

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
    return render(request, "index.html",{'student_data':student_data, 'school_data':school_data})

def search(request):
    search=request.POST['search']
    student_data= Student.objects.filter(Q(student_name=search) | Q(enrollment=search) | Q(school=search))
    return render(request,'index.html',{'student_data':student_data})



# For making API's
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



# Create your views here.
