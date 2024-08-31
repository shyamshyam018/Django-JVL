from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):
    blog_title = 'Latest News'
    blog_navbar = 'Sr Blogs'
    return render(request, 'blog/index.html',{'blog_title':blog_title,'blog_navbar':blog_navbar})

def detail(request,post_id):
    return render(request, 'blog/detail.html')

def old_url_redirect(request):
    return redirect(reverse('blog:new_url'))

def new_url(request):
    return HttpResponse("This is the new url")