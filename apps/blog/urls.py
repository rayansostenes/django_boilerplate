from django.urls import path, include
from apps.blog import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('post', views.PostModelViewSet)


app_name = 'blog'
urlpatterns = [
    path('', views.PostSearchView.as_view(), name='index'),
    path('', views.PostSearchView.as_view(), name='search'),
    path('api/', include(router.urls)),
    path('<slug>', views.PostDetailView.as_view(), name='detail'),
]


menu = [
    {'url': 'blog:index', 'title': 'Blog'},
    {'url': 'blog:index', 'title': 'Blog1'},
    {'url': 'blog:index', 'title': 'Blog2'},
    {'url': 'blog:index', 'title': 'Blog3'},
]