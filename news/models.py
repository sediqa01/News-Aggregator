from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
from datetime import datetime

User = get_user_model()

STATUS = ((0, "Draft"), (1, "Published"))


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.user.username


class Category(models.Model):
    category_name = models.CharField(max_length=25)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    news_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='news_article')
    news_image = CloudinaryField('image', default='placeholder')
    news_overview = models.TextField(null=True)
    news_content = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    news_categories = models.ManyToManyField(Category)
    published_status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='news_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.news_title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.news_title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    news = models.ForeignKey(Article, on_delete=models.CASCADE,
                             related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.user.username
