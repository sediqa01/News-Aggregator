from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic, View
from django.http import HttpResponseRedirect
from news.models import Article
from .forms import CommentForm, AddNewsForm, UpdateNewsForm
from django.views.generic.edit import FormView, CreateView, UpdateView


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
                "form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Article.objects.filter(published_status=1)
        news = get_object_or_404(queryset, slug=slug)
        comments = news.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if news.likes.filter(id=self.request.user.id).exists():
            liked = True

        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.instance.user = request.user
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


class Like(View):
    def post(self, request, slug, *args, **kwargs):
        news = get_object_or_404(Article, slug=slug)
        if news.likes.filter(id=request.user.id).exists():
            news.likes.remove(request.user)
        else:
            news.likes.add(request.user)

        return HttpResponseRedirect(reverse('article', args=[slug]))


class AddNewsPost(CreateView):
    model = Article
    template_name = 'add_news.html'
    form_class = AddNewsForm
    success_url = reverse_lazy('home')

# ----  later ----
    # def form_valid(self, form):
    #     author = Author.objects.get(user=self.request.user)
    #     form.instance.author = self.request.user
    #     form.save()
    #     return super(form_valid, self).form_valid(form)


class UpdateNewsPost(UpdateView):
    model = Article
    template_name = 'update_news.html'
    form_class = UpdateNewsForm
    success_url = reverse_lazy('home')
