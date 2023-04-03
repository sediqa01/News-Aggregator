from . import views
from django.urls import path


urlpatterns = [
    path("", views.NewsList.as_view(), name="home"),
    path('add_news/', views.AddNewsPost.as_view(), name='add_news'),
    path('news/edit/<slug:slug>', views.UpdateNews.as_view(), name='update'),
    path('news/delete/<slug:slug>', views.DeleteNews.as_view(), name='delete'),
    # path('signup/<slug:slug>', views.UserSignupForm.as_view(), name='signup'),
    path('news/<slug:slug>', views.NewsDetail.as_view(), name='article'),
    path('like/<slug:slug>', views.Like.as_view(), name='news_like'),
]
