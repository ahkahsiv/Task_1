from rest_framework import serializers
from . models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"

    


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields ="__all__"

    def to_representation(self, instance):
        context ={
            'school_name' : instance.school.school_name,
            'student_name' : instance.student_name,
            'enrollment' : instance.enrollment,
        }
        return context

