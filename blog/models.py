from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# author's profile 
class AuthourProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # AuthourProfile is connected to the built-in User model using a ForeignKey relationship, allowing us to associate each author profile with a specific user account.
    profile_picture = models.ImageField(upload_to='authors/')
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class BlogPostCategory(models.Model):
    name = models.CharField(max_length=10, unique=True) 
    description = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    category = models.ForeignKey(BlogPostCategory, on_delete=models.CASCADE)   

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # to connect a blog post to an authenticated user
    author = models.ForeignKey(AuthourProfile, on_delete=models.CASCADE, blank=True, null=True)  # using the author profile instead of the user model directly, to get data related to the author like profile picture and bio

    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Blog Title: {self.title}'
    
