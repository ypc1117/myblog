from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('upload', views.post_blog),
    path('comment', views.post_blog_comment),
    path('show', views.show_blog_detail)
]
