from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from courses.forms import CourseForm
from courses.models import Course


class CoursesListView(ListView):
    model = Course
    template_name = 'courses/courses_list.html'
    context_object_name = 'courses'


class CourseView(DetailView):
    model = Course
    queryset = Course.objects.prefetch_related('teachers').all()
    template_name = 'courses/show_course.html'
    context_object_name = 'course'


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/create_course.html'
    success_url = reverse_lazy('courses_list')


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/update_course.html'
    context_object_name = 'course'
    success_url = reverse_lazy('courses_list')


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/delete_course.html'
    context_object_name = 'course'
    success_url = reverse_lazy('courses_list')
