from django.urls import path
from apps.blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug>', views.PostDetailView.as_view(), name='detail'),
]

menu = [
    {'url': 'blog:index', 'title': 'Blog'},
    {'url': 'blog:index', 'title': 'Blog1'},
    {'url': 'blog:index', 'title': 'Blog2'},
    {'url': 'blog:index', 'title': 'Blog3'},
]