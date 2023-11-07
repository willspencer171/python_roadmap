from django.urls import path

from . import views

app_name = "Blogs"
urlpatterns = [
    path("", views.homepage, name="home"),
    path("blogs/<int:post_id>", views.view_blog, name="blog"),
    path("createblog", views.create_blog),
    path("login/", views.login_user, name="login_authorisation"),
]
