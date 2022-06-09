from django.contrib import admin
from .models import Message
from .models import Thread

admin.site.register(Thread)
admin.site.register(Message)