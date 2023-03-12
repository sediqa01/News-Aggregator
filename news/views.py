from django.shortcuts import render
from django.views import generic
from .models import Article


class NewsList(generic.ListView):
    model = Article

    queryset = Article.objects.filter(published_status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3
