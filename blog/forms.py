from django import forms
from . models import BlogPost
from django_summernote.widgets import SummernoteWidget

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['category','title','image','body','author'] # field to display in the form as input

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class':'form-input',
                    'placeholder':'Enter post title'
                }),
                'category': forms.Select(attrs={'class':'form-input'}),
                'author': forms.Select(attrs={'class':'form-input'}),
                'image': forms.FileInput(attrs={'class':'form-input-file'}),
                'body':SummernoteWidget(),
        }

