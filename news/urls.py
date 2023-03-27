from . import views
from django.urls import path


urlpatterns = [
    path("", views.NewsList.as_view(), name="home"),
    path('add_news/', views.AddNewsPost.as_view(), name='add_news'),
    path('news/<slug:slug>', views.NewsDetail.as_view(), name='article'),
    path('like/<slug:slug>', views.Like.as_view(), name='news_like'),
]
