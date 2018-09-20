from django.views.generic import ListView
from .models import Post

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'