from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import *

@login_required()
def home_view(request):
    books = Book.objects.all()
    return render(request, 'home.html', context={
        'books' : books,
        })
