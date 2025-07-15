from django.test import TestCase
from django.urls import reverse

from courses.models import Course


class CourseCRUDTests(TestCase):

    def test_courses_list_view(self):
        self.course1 = Course.objects.create(
            title='Основы Python',
            description='Базовый курс по программированию на Python'
        )
        self.course2 = Course.objects.create(
            title='Основы Java',
            description='Базовый курс по программированию на Java'
        )
        url = reverse('courses_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/courses_list.html')
        self.assertContains(response, 'Основы Python')
        self.assertContains(response, 'Основы Java')

    def test_course_create(self):
        response = self.client.post(
            reverse('course_create'),
            {
                'title': 'Основы C++',
                'description': 'Базовый курс по программированию на C++'
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Course.objects.filter(title='Основы C++').exists())

    def test_course_update(self):
        course = Course.objects.create(
            title='Основы C#',
            description='Базовый курс по программированию на C#'
        )
        response = self.client.post(
            reverse('course_update', args=[course.id]),
            {'title': 'New Основы C#'}
        )
        course.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(course.title, 'New Основы C#')

    def test_course_delete(self):
        course = Course.objects.create(
            title='Основы SQL',
            description='Базовый курс по SQL'
        )
        response = self.client.post(reverse('course_delete', args=[course.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Course.objects.filter(title='Основы SQL').exists())
