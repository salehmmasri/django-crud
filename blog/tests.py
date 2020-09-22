from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.
class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='saleh',
            email='salehalmasri@yahoo.com',
            password='password'
        )
        self.post = Post.objects.create(
            title='Love',
            author=self.user,
            body='Nothing',
        )
    def test_blog_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_details_view(self):
        response = self.client.get(reverse('detail_view', args='1'))
        self.assertEqual(response.status_code, 200)
    def test_update_view(self):
        response = self.client.post(reverse('blog_update', args='1'), {
            'title': 'Love',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Love')
    def test_create_view(self):
        response = self.client.post(reverse('blog_create'), {
            'title': 'Nolove',
            'author': self.user,
            'body' :'Nolove',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nolove')
        self.assertContains(response, 'Nolove')
        self.assertContains(response, 'saleh')
    def test_delete_view(self):
        response = self.client.get(reverse('blog_delete', args='1'))
        self.assertEqual(response.status_code, 200)
        post_response = self.client.post(reverse('blog_delete', args='1'))
        self.assertRedirects(post_response, reverse('home'), status_code=302)