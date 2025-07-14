from django.conf import settings
from django.core.mail import send_mail


def send_admin_notification(email, first_name, last_name, description):
    subject = 'Новое сообщение от пользователя'
    message = (
        f'Получено новое сообщение:\n\n'
        f'Имя: {first_name}\n'
        f'Фамилия: {last_name}\n'
        f'Email: {email}\n\n'
        f'Сообщение:\n'
        f'{description}'
    )
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.EMAIL_ADMIN],
        fail_silently=False,
    )

def send_user_confirmation(email, first_name):
    subject = 'Ваше сообщение получено'
    message = (
        f'Уважаемый(ая) {first_name},\n\n'
        'Благодарим вас за ваше сообщение. '
        'Мы рассмотрим его в ближайшее время\n'
        'и свяжемся с вами при необходимости.\n\n'
        'С уважением,\n'
        'Команда "Курсы - онлайн"'
    )
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
