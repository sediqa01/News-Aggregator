from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from news.models import Article
from .forms import CommentsForm


class NewsList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(
        published_status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class NewsDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(slug=slug)
        news = get_object_or_404(queryset, slug=slug)
        comments = news.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if news.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "article.html",
            {
                "article": news,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "form": CommentsForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Article.objects.filter(status=1)
        news = get_object_or_404(queryset, slug=slug)
        comments = news.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if news.likes.filter(id=self.request.user.id).exists():
            liked = True

        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.instance.user = request.user.username
            comment = form.save(commit=False)
            comment.news = news
            comment.save()
        else:
            form = CommentForm()

        return render( 
            request,
            "article.html",
            {
                "article": news,
                "comments": comments,
                "commented": True,
                "form": form,
                "liked": liked
            },
        )