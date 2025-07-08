from django import forms

from training_website.courses.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'teachers']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'teachers': 'Учителя',
            }
        widgets = {
            'teachers': forms.SelectMultiple(attrs={'class': 'form-select'})
        }
