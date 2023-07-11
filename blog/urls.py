from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('account/create', views.blog_upload, name='create_post'),
    path('post_detail/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('delete/<slug:slug>', views.PostDelete.as_view(), name='post_delete'),
]
