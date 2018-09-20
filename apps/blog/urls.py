from django.urls import path
from apps.blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]