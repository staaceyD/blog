from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class CreatePost(generic.CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'slug', 'author', 'content']


class UpdatePost(generic.UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'slug', 'content']


class Add(generic.CreateView):
    model = Post
    template_name = 'add.html'
    fields = ['title', 'slug', 'author', 'content']