from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def homepage(request):
    current_user = request.user
    context = {
        "user": current_user
    }

    return render(request, "index.html", context)

def view_blog(request, post_id):
    current_user = request.user
    blog_post = get_object_or_404(BlogPost, pk=post_id)

    context = {
        "user": current_user,
        "post": blog_post
    }

    return render(request, "blogs.html", context)

def create_blog(request):
    
    context = {

    }
    
    return render(request, "create_blog.html", context)
