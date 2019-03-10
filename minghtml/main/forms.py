from django import forms
from main.models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='功課', max_length=128)
    content = forms.CharField(label='內容', widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ['title', 'content']