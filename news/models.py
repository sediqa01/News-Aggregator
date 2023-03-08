from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

User = get_user_model()


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
    news_overview = RichTextField(blank=True, null=True)
    news_content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    news_categories = models.ManyToManyField(Category)
    published = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        User, related_name='news_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.news_title

    def number_of_likes(self):
        return self.likes.count()
