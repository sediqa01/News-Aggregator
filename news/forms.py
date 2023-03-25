from django import forms
from news.models import Comment


class CommentsForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Write a comment ...',
        'rows': '4',

    }))

    class Meta:
        model = Comment
        fields = ('content',)
