from django.test import TestCase
from .forms import CommentForm, BlogForm


class TestCommentForm(TestCase):

    def test_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_body_is_not_required(self):
        form = CommentForm({'body': 'Hi There!'})
        self.assertTrue(form.is_valid())


class TestBlogForm(TestCase):

    def test_form_content_required(self):
        form = BlogForm({'title': '', 'content': '', 'category': ''})
        self.assertFalse(form.is_valid())

    def test_form_content_not_required(self):
        form = BlogForm({'title': 'name', 'content': 'text input here', 'category': 'any'})
        self.assertTrue(form.is_valid)

