from django.core.mail import get_connection


def smtp():
    connection = get_connection(
        host='smtp.gmail.com',
        port=587,
        username='givbox24@gmail.com',
        password='ooqx tcai uvcy mbtb',
        use_tls=True,
    )
    return connection
