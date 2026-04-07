from django.shortcuts import render
from . import models
# Create your views here.

# blog_posts = models.BlogPost.objects.all()  # to get all the blog posts from the database and store them in a variable called blog_posts, which can be used in the template to display the list of blog posts.

def blog_index(request):
    blog_posts = models.BlogPost.objects.all()  # to get all the blog posts from the database and store them in a variable called blog_posts, which can be used in the template to display the list of blog posts.
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'blog.html', context) 


def blog_detail(request, blog_id):
    blog_post = models.BlogPost.objects.get(id=blog_id)  # to get a specific blog post from the database based on the blog_id parameter passed in the URL and store it in a variable called blog_post, which can be used in the template to display the details of that specific blog post.
    context = {
        'blog_post': blog_post
    }
    return render(request, 'blog/blog-detail.html', context)
