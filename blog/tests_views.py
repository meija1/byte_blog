from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Category, Comment, User
import json

class TestViews(TestCase):

    def setUp(self):
        self.post_detail = reverse('post_detail', args=['post'])
        self.user = User.objects.create(username='testuser',password='secret',is_active=True)
        self.apps = Category.objects.create(name='Apps', slug='Apps')
        self.post = Post.objects.create(title='post',content='post',author=self.user,status=1,category=self.apps)

    def test_homepage_GET(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_post_detail_GET_view(self):
        response = self.client.get(self.post_detail)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_detail_POST_view(self):
        self.comment = Comment.objects.create(post=self.post, body='Testing', approved=True)
        response = self.client.post(self.post_detail)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.comment.post.title, 'post')

    def test_post_detail_POST_no_data(self):
        comment = Comment.objects.create(post=self.post, body='')
        response = self.client.post(self.post_detail)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(comment.body, '')

    def test_post_upload_POST_view(self):
        response = self.client.post('/create', {'title': 'test', 'content': 'test', 'category': 'apps'})
        self.assertEquals(response.status_code, 301)

    def test_category_view(self):
        response = self.client.get(reverse('category', args=[self.apps]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')


    def test_post_update_view(self):
        self.code = Category.objects.create(name='Code', slug='Code')
        response = self.client.post(reverse('post_update', args=[self.post.slug]),{'title': 'updatedtest', 'content': 'updatedcontent', 'category': self.code.id})
        self.assertEquals(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEquals(self.post.title, 'updatedtest')
        

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=(self.post.slug,)), follow=True)
        self.assertEquals(response.status_code, 200)
        deleted_post = Post.objects.filter(slug=self.post.slug)
        self.assertEqual(len(deleted_post), 0)

    
