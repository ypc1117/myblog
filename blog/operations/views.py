import json
import datetime

from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog, BlogComment

# Create your views here.

def index(request):
    return HttpResponse("Hello, This is a  my first blog")


def show_blog_detail(request):
    if request.method=="GET":
        blogs = []
        callback = request.GET.get('callback')
        for blog in Blog.objects.all():
            blog_detail = {}
            blog_detail['id'] = blog.id
            blog_detail['title'] = blog.title
            blog_detail['content'] = blog.content
            blog_comments = []
            for blog_comment in BlogComment.objects.all().filter(blog_id=blog.id):
                comment_detail = {}
                comment_detail['nickname'] = blog_comment.nickname
                comment_detail['comment'] = blog_comment.comment
                comment_detail['created_time'] = blog_comment.created_time.strftime("%Y-%m-%d-%H")
                blog_comments.append(comment_detail)
            blogs.append({
                "id": blog.id,
                "blog":blog_detail,
                "comments":blog_comments
            })
        return HttpResponse(('%s(%s)') % (callback, json.dumps(blogs, indent=4)))


def post_blog(request):
    form = request.body
    if request.method=="GET":
        print("your http method is get!!!")
    else:
        print("your http method is post!!!")
        title = request.POST.get('title')
        content = request.POST.get('content')
        blog = Blog.objects.create(title=title, content=content)
        blog.save()
    return HttpResponse("Hello, you may need to come on for yourself")

def post_blog_comment(request):
    form = request.body
    if request.method=="GET":
        print("your http method is get!!!")
    else:
        print("your http method is post!!!")
        blog_id = request.POST.get('blog_id')
        comment = request.POST.get('comment')
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        blog_comment = BlogComment.objects.create(blog_id=blog_id, comment=comment, email=email, nickname=nickname)
        blog_comment.save()
    return HttpResponse("Hello, you may need to come on for yourself")

