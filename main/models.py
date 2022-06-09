from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Thread(models.Model):
    participants = models.ManyToManyField(User, verbose_name="Members")
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)


class Message(models.Model):
    sender = models.ForeignKey(User, verbose_name="Sender", on_delete=models.CASCADE)
    text = models.TextField("Message")
    thread = models.ForeignKey(Thread, verbose_name="Chat", on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=True)


