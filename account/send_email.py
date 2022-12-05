from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f'http://127.0.0.1/accounts/activate/{code}/'
    send_mail(
        'Hello! Activate your account!',
        f'To activate your account you need to link: {full_link}',
        'toktobekkyzysirin@gmail.com',
        [user],
        fail_silently=False
    )

