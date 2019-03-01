from django import forms
from .models import ArticleColumn, ArticlePost,ArticleTag, Comment

class ArticleColumnForm(forms.ModelForm): 
    class Meta:
        model = ArticleColumn 
        fields = ("column",)


class ArticlePostForm(forms.ModelForm): 
    class Meta:
        model = ArticlePost 
        fields = ("title", "body")


class ArticleTagForm(forms.ModelForm):
    class Meta:
        model = ArticleTag 
        fields = ('tag', )


class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = ("commentator", "body",)
        widgets = {
            'commentator': forms.widgets.TextInput(attrs={'autocomplete':'off','placeholder':'评论员'}),

        }

