from django.urls import path
from . import views

urlpatterns=[
    path("", views.blog_view, name='blog'),
    path("add_post/",views.blog_from_view,name='blog_form'),
    path("blog_detail/<int:id>/",views.blog_detail_view,name='Full_view'),
]