from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
