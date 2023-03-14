from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from news.models import Article


class NewsList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(
        published_status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 9


class NewsDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        news = get_object_or_404(queryset, slug=slug)
        liked = False
        if news.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "article.html",
            {
                "news": news,
                "liked": liked
            },
        )
