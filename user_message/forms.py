from django import forms

from user_message.models import UserMessage


class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ['first_name', 'last_name', 'email', 'description']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Почта',
            'description': 'Сообщение',
            }
