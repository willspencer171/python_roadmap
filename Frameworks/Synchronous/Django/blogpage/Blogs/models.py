from typing import Any
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=16)
    second_name = models.CharField(max_length=16)
    username = models.CharField(max_length=16, unique=True)
    
    @property
    def user_blogs(self):
        return self.blogpost_set.all()
    
    def __str__(self) -> str:
        return self.username

class Category(models.Model):
    category_name = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.category_name

class BlogPost(models.Model):
    blog_author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=64)
    blog_content = models.TextField(max_length=255)
    posted_at = models.DateTimeField(default=timezone.now, editable=False)
    category = models.ManyToManyField(Category)

    blogs = models.Manager()

    def __str__(self) -> str:
        return self.title +" posted by " + self.blog_author.username + " on " + self.posted_at.strftime("%d-%m-%Y, at %H:%M:%S ") + self.posted_at.tzname()

class Comment(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.TextField(max_length=255)
    posted_at = models.DateTimeField(default=timezone.now, editable=False)
    comment_blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True)

    comments = models.Manager()
    
    def __str__(self) -> str:
        return "Comment posted by " + self.comment_author.username + " on " + self.posted_at.strftime("%d-%m-%Y, at %H:%M:%S ") + self.posted_at.tzname() + " on " + self.comment_blog.title
