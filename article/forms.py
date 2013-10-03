from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    # form used to create new article
    class Meta:
        model = Article
        fields = ('pub_date', 'title', 'body', 'thumbnail')
        
        
class CommentForm(forms.ModelForm):
    # form used to leave a comment
    class Meta:
        model = Comment
        fields = ('name', 'body')
        
        