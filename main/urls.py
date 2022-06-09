from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('str_messages', views.str_messages),
    path('str_thread', views.str_thread),
    path('mark', views.mark),
    path('unread', views.unread)
]