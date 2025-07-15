from django.db import models

from teachers.models import Teacher


class Course(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False
    )
    description = models.TextField(
        max_length=1000,
        blank=True
    )
    teachers = models.ManyToManyField(
        Teacher,
        related_name='courses',
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False
    )
    content = models.TextField(
        null=False,
        blank=False,
        max_length=10000
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
