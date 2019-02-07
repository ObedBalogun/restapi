from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from postings.models import BlogPost
#test can be automated
#it has/ is a blank database

User = get_user_model()

class BlogPostAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User.objects.create(username = 'text_obed', email='test@test.com')
        user_obj.set_password("random")
        user_obj.save()
        blog_post = BlogPost.objects.create(
            user = user_obj,
            title='New title',
            content="Rando Content"
        )

        def test_single_user(self):
            user_count = User.objects.count()
            self.assertEqual(user_count,1)