from . import views
from django.urls import path
from .views import PostUpload


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.PostUpload.as_view(), name='create_post'),
]
