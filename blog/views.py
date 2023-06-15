from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentForm
from . import forms


''' Create a basic view for the website '''
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"
    paginate_by = 6

''' Add view for post details '''
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
            queryset = Post.objects.filter(status=1)
            post = get_object_or_404(queryset, slug=slug)
            comments = post.comments.filter(approved=True).order_by('-created_on')
            liked = False
            if post.likes.filter(id=self.request.user.id).exists():
                liked =True

            return render(
                request, "post_detail.html", {"post": post, "comments": comments, "liked": liked, "comment_form": CommentForm()},
            )


class PostUpload(View):

    def blog_upload(request):
        blog_form = forms.BlogForm()
        if request.method == 'POST':
            blog_form = forms.BlogForm(request.POST)
            if blog_form.is_valid():
                blog_form.save
        context = {
                'blog_form': blog_form,
            }
        return render(request, "account/create_post.html", context=context)
