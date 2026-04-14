from django import forms
from . models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['category','title','image','body','author'] # field to display in the form as input

