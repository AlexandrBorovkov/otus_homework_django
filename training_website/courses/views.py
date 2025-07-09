from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from training_website.courses.forms import CourseForm
from training_website.courses.models import Course


class CoursesListView(View):
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        return render(
            request,
            'courses/courses_list.html',
            context={
                'courses': courses,
            },
        )

class CourseView(View):
    def get(self, request, *args, **kwargs):
        course_id = kwargs.get('id')
        course = get_object_or_404(
            Course.objects.prefetch_related('teachers'),
            id=course_id
        )
        return render(
            request,
            'courses/show_course.html',
            context={
                'course': course,
            },
        )

class CourseCreateView(View):
    def get(self, request, *args, **kwargs):
        form = CourseForm()
        return render(request, 'courses/create_course.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Курс успешно создан')
            return redirect('courses_list')
        return render(request, 'courses/create_course.html', {'form': form})

class CourseUpdateView(View):
    def get(self, request, *args, **kwargs):
        course_id = kwargs.get('id')
        course = get_object_or_404(
            Course.objects.prefetch_related('teachers'),
            id=course_id
        )
        form = CourseForm(instance=course)
        return render(
            request,
            'courses/update_course.html',
            {'form': form, 'course_id': course_id}
            )

    def post(self, request, *args, **kwargs):
        course_id = kwargs.get('id')
        course = Course.objects.get(id=course_id)
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Курс успешно обнавлен')
            return redirect('courses_list')
        return render(
            request,
            'courses/update_course.html',
            {'form': form, 'course_id': course_id}
            )

class CourseDeleteView(View):
    def get(self, request, *args, **kwargs):
        course_id = kwargs.get('id')
        return render(
            request,
            'courses/delete_course.html',
            {'course_id': course_id}
        )

    def post(self, request, *args, **kwargs):
        course_id = kwargs.get('id')
        course = Course.objects.get(id=course_id)
        if course:
            course.delete()
            messages.success(request, 'Курс успешно удален')
        return redirect('courses_list')
