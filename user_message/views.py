from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from user_message.forms import UserMessageForm


class UserMessageView(View):
    def get(self, request, *args, **kwargs):
        form = UserMessageForm()
        return render(request, 'user_message/user_message.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение отправленно')
            return redirect('index')
        return render(request, 'courses/create_course.html', {'form': form})
