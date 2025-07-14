from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from teachers.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        'email'
    )
    search_fields = ["last_name"]
    list_filter = (
        ("date_joined", DateFieldListFilter),
    )
