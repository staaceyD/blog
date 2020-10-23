from .views import PostList, PostDetail, UpdatePost, Add, DeletePost
from django.urls import path

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('edit/<slug:slug>/', UpdatePost.as_view(), name='update_post'),
    path('add', Add.as_view(), name='add'),
    path('delete/<slug:slug>/', DeletePost.as_view(), name='delete'),

]
