from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog-single.html', views.blog_single, name="blog-single"),
    path('blog.html', views.blog, name="blog"),
    path('project.html', views.project, name="project"),
]