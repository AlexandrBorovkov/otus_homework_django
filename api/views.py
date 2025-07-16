from django.db.models import Prefetch
from rest_framework import response, views

from api.serializers import CourseSerializer
from courses.models import Course
from teachers.models import Teacher


class CoursesList(views.APIView):
    def get(self, request):
        queryset = Course.objects.prefetch_related(
            Prefetch('teachers', queryset=Teacher.objects.all())
        ).all()
        serializer = CourseSerializer(instance=queryset, many=True)
        response_json = serializer.data
        return response.Response(response_json)
