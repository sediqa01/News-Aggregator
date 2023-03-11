from django.shortcuts import render
from django.views import generic
from .models import Article


def base(request):
    return render(request, 'base.html', {})