from django.urls import path

from user_message import views

urlpatterns = [
    path('', views.UserMessageView.as_view(), name='user_message'),
]
