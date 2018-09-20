from django.views.generic import ListView, DetailView
from .models import Post

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detalhe.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'