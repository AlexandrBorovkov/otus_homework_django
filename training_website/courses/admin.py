from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from training_website.courses.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "teachers_list"
    )
    search_fields = ["title"]
    list_filter = (
        ("created_at", DateFieldListFilter),
    )

    def teachers_list(self, obj):
        teachers = obj.teachers.all()
        return ", ".join([teacher.get_full_name() for teacher in teachers])

admin.site.register(Lesson)
