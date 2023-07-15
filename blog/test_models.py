from django.test import TestCase
from .models import Post, Category, Comment, User

class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='testuser', password='secret', is_active=True)
        self.apps = Category.objects.create(name='Apps', slug='Apps')
        self.post = Post.objects.create(
            title='post', content='post', author=self.user, status=1, category=self.apps)
        self.comment = Comment.objects.create(post=self.post, body='test', name=self.user, approved=True)


    def test_post_name_equals_slug_name_on_creation(self):
        self.assertEquals(self.post.slug, 'post')


    def test_category_contains_same_slug_name(self):
        self.assertEquals(self.apps.slug, 'Apps')
