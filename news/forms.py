from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from news.models import Comment, Article
from django_summernote.widgets import SummernoteWidget


# from django-allauth's SignupForm
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        def __init__(self, *args, **kwargs):
            super(SignupForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['class'] = 'form-control'


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Write a comment ...',
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ('content',)


class AddNewsForm(forms.ModelForm):
    news_overview = forms.CharField(widget=SummernoteWidget())
    news_content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Article
        fields = (
            'news_title', 'author', 'news_image', 'news_overview',
            'news_content', 'news_categories', 'published_status')

        widgets = {
            'news_title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'news_overview': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write content here ...',
            }),
            'news_content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write content here ...',
            }),
            'news_categories': forms.SelectMultiple(
                                attrs={'class': 'form-select'}),
            'published_status': forms.Select(attrs={'class': 'form-control'}),
        }


class UpdateNewsForm(forms.ModelForm):
    news_overview = forms.CharField(widget=SummernoteWidget())
    news_content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Article
        fields = (
            'news_title', 'news_image', 'news_overview',
            'news_content', 'news_categories', 'published_status')

        widgets = {
            'news_title': forms.TextInput(attrs={'class': 'form-control'}),
            'news_overview': forms.Textarea(attrs={'class': 'form-control'}),
            'news_content': forms.Textarea(attrs={'class': 'form-control'}),
            'news_categories': forms.SelectMultiple(
                                attrs={'class': 'form-select'}),
            'published_status': forms.Select(attrs={'class': 'form-control'}),
        }
