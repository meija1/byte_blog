from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import PostList, PostDetail, PostUpdate, blog_upload, category, PostLike, PostDelete

class TestUrls(TestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, PostList)

    def test_post_detail_is_resolved(self):
        url = reverse('post_detail', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, PostDetail)

    def test_post_update_is_resolved(self):
        url = reverse('post_update', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, PostUpdate)

    def test_create_post_is_resolved(self):
        url = reverse('create_post')
        self.assertEquals(resolve(url).func, blog_upload)

    def test_post_category_is_resolved(self):
        url = reverse('category', args=['slug'])
        self.assertEquals(resolve(url).func, category)

    def test_post_like_is_resolved(self):
        url = reverse('post_like', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, PostLike)

    def test_post_delete_is_resolved(self):
        url = reverse('post_delete', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, PostDelete)

