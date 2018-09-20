from django.db.models import Q
from django.views.generic import ListView, DetailView
from rest_framework.viewsets import ModelViewSet


from .models import Post
from .serializers import PostSerializer

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detalhe.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class PostSearchView(IndexView):
    def get_queryset(self):
        original_qs = super().get_queryset()
        termo = self.request.GET.get('q', None)
        if termo is None:
            return original_qs
        query = Q(title__icontains=termo) | Q(body__icontains=termo)
        return original_qs.filter(query)


class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all() 