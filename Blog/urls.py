from django.urls import path
from Blog.views import Blog, Blog_detail

urlpatterns = [
    path('', Blog, name='blog'),
    path('blog_detail/<slug>', Blog_detail, name='blog_detail')
]