from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django_rq import get_queue

from user_message.forms import UserMessageForm
from user_message.tasks import send_admin_notification, send_user_confirmation


class UserMessageView(View):
    def get(self, request, *args, **kwargs):
        form = UserMessageForm()
        return render(request, 'user_message/user_message.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserMessageForm(request.POST)
        if form.is_valid():
            user_message = form.save()

            queue = get_queue('default')

            queue.enqueue(
                send_admin_notification,
                user_message.email,
                user_message.first_name,
                user_message.last_name,
                user_message.description
            )

            queue.enqueue(
                send_user_confirmation,
                user_message.email,
                user_message.first_name
            )

            messages.success(request, 'Сообщение отправленно')
            return redirect('index')
        return render(request, 'courses/create_course.html', {'form': form})
