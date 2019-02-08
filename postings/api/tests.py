from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from postings.models import BlogPost
#test can be automated
#it has/ is a blank database

User = get_user_model()         #self explanatory

class BlogPostAPITestCase(APITestCase):
    #setting up test data
    def setUp(self):
        #user_obj = User.objects.create(username = 'test_obed', email='test@test.com')
        user_obj = User(username = 'test_obed', email='test@test.com')
        user_obj.set_password("random")
        user_obj.save()
        blog_post = BlogPost.objects.create(
            user = user_obj,
            title='New title',
            content="Random Content"
        )
#running the test
    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count,1)
    def test_single_post(self):
        post_count = BlogPost.objects.count()
        self.assertEqual(post_count,1)









'''When testing in this case you create stuff like users,blogposts etc
basically you create instances of things that interact with your app'''