from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def blog_single(request):
    return render(request, 'blog-single.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def project(request):
    return render(request, 'project.html', {})