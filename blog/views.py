from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Post, Category
from .forms import CommentForm, BlogForm
from . import forms


''' Create a basic view for the website '''
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"

''' Add view for post details '''
class PostDetail(View):

    def get(self, request, id, *args, **kwargs):
            queryset = Post.objects.filter(status=1)
            post = get_object_or_404(queryset, id=id)
            comments = post.comments.filter(approved=True).order_by('-created_on')
            category = Category.objects.filter(slug=self)
            liked = False
            if post.likes.filter(id=self.request.user.id).exists():
                liked =True

            return render(
                request, "post_detail.html", {"post": post, "comments": comments, "category": category, "commented": False, "liked": liked, "comment_form": CommentForm()},
            )
            
            
    def post(self, request, id, *args, **kwargs):
            queryset = Post.objects.filter(status=1)
            post = get_object_or_404(queryset, id=id)
            comments = post.comments.filter(approved=True).order_by('-created_on')
            liked = False
            if post.likes.filter(id=self.request.user.id).exists():
                liked =True

            comment_form = CommentForm(data=request.POST)

            if comment_form.is_valid():
                comment_form.instance.email = request.user.email
                comment_form.instance.name = request.user.username
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
            else:
                comment_form = CommentForm()

            return render(
                request, "post_detail.html", {"post": post, "comments": comments, "commented": True, "liked": liked, "comment_form": CommentForm()},
            )

class PostUpload(View):

    def blog_upload(request):

        queryset = Post.objects.all()
        blog_form = BlogForm()
        if request.method == 'POST':
            blog_form = BlogForm(request.POST)
            if blog_form.is_valid():
                form = blog_form.save(commit=False)
                form.author = request.user
                form.post = queryset
                form.save()
                blog_form.save_m2m()
                
                return redirect('home')
            else:
                blog_form = BlogForm()

        return render(request, "account/create_post.html", {"blog_form": blog_form})


class CategoryView(View):

    def category(request, slug):

        post = Post.objects.filter(category_slug=slug).filter(status=1)
        category = Category.objects.get(slug=slug)
        categories = Category.objects.all()

        return render(request, "base.html", {"post": post, "category": category, "categories": categories})

        