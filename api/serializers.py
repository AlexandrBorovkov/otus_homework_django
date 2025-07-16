from rest_framework import serializers

from courses.models import Course
from teachers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name']


class CourseSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = '__all__'
