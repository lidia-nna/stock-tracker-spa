from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from ..mail import mail
from flask import render_template
import os
from ..config import DevConfig


class Token:
    def __init__(self, cfg=DevConfig):
        self.key = cfg.SECRET_KEY
        self.passw = os.environ.get('SECURITY_PASSWORD_SALT')
        self.sender = cfg.MAIL_DEFAULT_SENDER


    def generate_confirmation_token(self, email):
        serializer = URLSafeTimedSerializer(self.key)
        return serializer.dumps(email, salt=self.passw)


    def confirm_token(self, token, expiration=3600):
        serializer = URLSafeTimedSerializer(self.key)
        try:
            email = serializer.loads(
                token,
                salt=self.passw,
                max_age=expiration
            )
        except:
            return False
        else:
            return email

class Email(Token):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def send_email(self, to, subject, template):
        msg = Message(
            subject,
            recipients=[to],
            html=template,
            sender=self.sender
        )
        mail.send(msg)
        return "Message sent"