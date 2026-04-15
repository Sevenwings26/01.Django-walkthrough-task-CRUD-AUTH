from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


"""
CRUD Operation
Create
Read
Update
Delete
"""

# Create your views here.

# blog_posts = models.BlogPost.objects.all()  # to get all the blog posts from the database and store them in a variable called blog_posts, which can be used in the template to display the list of blog posts.

def blog_index(request):
    blog_posts = models.BlogPost.objects.all()  # to get all the blog posts from the database and store them in a variable called blog_posts, which can be used in the template to display the list of blog posts.

    # update to paginate 
    paginator = Paginator(blog_posts, 3)
    # for page to work 
    page = request.GET.get('page')

    # error handling 
    try:
        blogs_page = paginator.page(page)
    except PageNotAnInteger:
        blogs_page = paginator.page(1)
    except EmptyPage:
        blogs_page = paginator.page(paginator.num_pages)


    context = {
        'blog_posts': blogs_page
    }
    return render(request, 'blog.html', context) 


def blog_detail(request, blog_id):
    blog_post = models.BlogPost.objects.get(id=blog_id)  # to get a specific blog post from the database based on the blog_id parameter passed in the URL and store it in a variable called blog_post, which can be used in the template to display the details of that specific blog post.
    context = {
        'blog_post': blog_post
    }
    return render(request, 'blog/blog-detail.html', context)

from . forms import BlogPostForm 
# Create a blog 
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog-index')
    else:
        form = BlogPostForm()
    context = {'form':form, 'title':'Create'}
    return render(request, 'blog/blog-create.html', context)
    

# Update a blog 
def blog_update(request, id):
    blog_post = get_object_or_404(models.BlogPost, pk=id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('blog-index')
    else:
        form = BlogPostForm(instance=blog_post)
    context = {
        'form':form,
        'blog_post':blog_post,
        'title':'Update'
        }
    return render(request, 'blog/blog-create.html', context)

def blog_delete(request, id):
    blog_post = get_object_or_404(models.BlogPost, pk=id)
    if request.method == 'POST':
        blog_post.delete()
        return redirect('blog-index')
    return render(request, 'blog/blog-delete.html', {'blog_post':blog_post})




# # CREATE & UPDATE (Combined logic)
# def post_upsert(request, pk=None):
#     if pk:
#         post = get_object_or_404(models.BlogPost, pk=pk)
#         title = "Edit Post"
#     else:
#         post = models.BlogPost()
#         title = "New Post"

#     if request.method == 'POST':
#         # request.FILES is mandatory for image uploads
#         form = BlogPostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = BlogPostForm(instance=post)
    
#     return render(request, 'blog/post_form.html', {'form': form, 'title': title})




# Using Class 
"""
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import BlogPostForm

# READ (List)
class PostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# READ (Detail)
class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'

# CREATE
class PostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

# UPDATE
class PostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

# DELETE
class PostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
"""