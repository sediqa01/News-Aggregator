from django import forms
from news.models import Comment, Article
from django_summernote.widgets import SummernoteWidget


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
            'news_title', 'news_image', 'news_overview',
            'news_content', 'news_categories', 'published_status')

        widgets = {
            'news_title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
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
