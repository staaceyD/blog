from .views import PostList, PostDetail, CreatePost, UpdatePost, Add
from django.urls import path

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('edit/<slug:slug>/', UpdatePost.as_view(), name='update_post'),
    path('add', Add.as_view(), name='add'),
]
