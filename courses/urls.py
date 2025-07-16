from django.urls import path

from courses import views

urlpatterns = [
    path('', views.CoursesListView.as_view(), name='courses_list'),
    path('<int:pk>/', views.CourseView.as_view(), name='course_view'),
    path('create/', views.CourseCreateView.as_view(), name='course_create'),
    path(
        '<int:pk>/update/',
        views.CourseUpdateView.as_view(),
        name='course_update'
    ),
    path(
        '<int:pk>/delete/',
        views.CourseDeleteView.as_view(),
        name='course_delete'
    ),
]
