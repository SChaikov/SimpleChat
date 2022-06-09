from django.shortcuts import render
from django.http import HttpResponse
from .models import Thread
from .forms import ThreadForm


def index(request):
    return render(request, 'main/index.html')


def create(request):
    form = ThreadForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


def str_thread(request):
    str_thr = Thread.objects.order_by('-id')
    return render(request, 'main/str_thread.html', {'title': 'Список объектов', 'objects': str_thr})


def str_messages(request):
    return HttpResponse("<h4>URL для - получения списка Messages</h4>")


def mark(request):
    return HttpResponse("<h4>URL для Marks Messages</h4>")


def unread(request):
    return HttpResponse("<h4>URL для Unread Messages</h4>")