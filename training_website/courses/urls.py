from django.urls import path

from training_website.courses import views

urlpatterns = [
    path("", views.CoursesListView.as_view(), name="courses_list"),
    path('<int:id>/', views.CourseView.as_view(), name="course_view"),
    path('create/', views.CourseCreateView.as_view(), name="course_create"),
    path(
        '<int:id>/update/',
        views.CourseUpdateView.as_view(),
        name="course_update"
    ),
    path(
        '<int:id>/delete/',
        views.CourseDeleteView.as_view(),
        name="course_delete"
    ),
]
