from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, Profile
from .forms import PostForm, CommentForm

# Tests for models
class ModelsTest(TestCase):
    def setUp(self):
        # Set up a user, post, and comment for testing
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(title='Sample Post', body='Test body', author=self.user)
        self.comment = Comment.objects.create(post=self.post, author=self.user, text='Nice comment!')

    def test_post_creation(self):
        # Test that a post is created with correct data
        self.assertEqual(self.post.title, 'Sample Post')
        self.assertEqual(self.post.author, self.user)

    def test_comment_creation(self):
        # Test that a comment is created with correct data
        self.assertEqual(self.comment.text, 'Nice comment!')
        self.assertEqual(self.comment.post, self.post)

    def test_profile_creation(self):
        # Test that a profile is automatically created for a user
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

# Tests for views
class ViewsTest(TestCase):
    def setUp(self):
        # Set up a logged-in user and a sample post for testing
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.post = Post.objects.create(title='Sample Post', body='Test body', author=self.user)

    def test_post_list_view(self):
        # Test the post list view
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sample Post')

    def test_post_create_view(self):
        # Test the post create view
        response = self.client.post(reverse('create_post'), {
            'title': 'New Post',
            'body': 'New content',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Post.objects.filter(title='New Post').exists())

# Tests for forms
class FormsTest(TestCase):
    def test_post_form_valid(self):
        # Test that PostForm is valid with correct data
        form = PostForm(data={'title': 'Test Title', 'body': 'Test Body'})
        self.assertTrue(form.is_valid())

    def test_comment_form_valid(self):
        # Test that CommentForm is valid with correct data
        form = CommentForm(data={'text': 'Test Comment'})
        self.assertTrue(form.is_valid())

# Tests for URLs
class URLsTest(TestCase):
    def test_post_list_url(self):
        # Test that the post list URL resolves correctly
        url = reverse('post_list')
        self.assertEqual(url, '/')  # Assuming root URL is the post list

    def test_post_detail_url(self):
        # Test that the post detail URL resolves correctly
        url = reverse('post_detail', args=[1])
        self.assertEqual(url, '/post/1/')  # Adjust based on your URL pattern
