from . import views
from django.urls import path


urlpatterns = [
    path("", views.NewsList.as_view(), name="home"),
    path('<slug:slug>/', views.NewsDetail.as_view(), name='article'),
]