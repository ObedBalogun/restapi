from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
#test authenticated user
from rest_framework_jwt.settings import api_settings

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

from postings.models import BlogPost
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

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

    def test_get_list(self):
        # test get list
        data = {}
        url = api_reverse('api-postings:post-listcreate')
        response = self.client.get(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)


    def test_post_item(self):
    # test get list
        data = {"title":"Some random title", "content":"more random content"}
        url = api_reverse('api-postings:post-listcreate')
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_item(self):
            # test get list
            blog_post = BlogPost.objects.first()
            data = {}
            url = blog_post.get_api_url()
            response = self.client.get(url,data,format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            print(response.data)


    def test_update_item(self):
    # test get list
        blog_post = BlogPost.objects.first()
        url = blog_post.get_api_url()
        data = {"title":"Some random title", "content":"more random content"}
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_update_item_with_user(self):
        # test get list
        blog_post = BlogPost.objects.first()
        print(blog_post.content)
        url = blog_post.get_api_url()
        data = {"title":"Some random title", "content":"more random content"}
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION = 'JWT '+ token_rsp)
        #Anytime you make a request related to your user, you have to pass in a token

        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_post_item_with_user(self):
    # test get list
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)
        data = {"title":"Some random title", "content":"more random content"}
        url = api_reverse('api-postings:post-listcreate')
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_user_ownership(self):
        # test get list
        owner = User.objects.create(username='testuser2')
        blog_post = BlogPost.objects.create(
            user = owner,
            title = 'New title',
            content = 'another random_content'
        )
        user_obj = User.objects.first()
        self.assertNotEqual(user_obj.username, owner.username)
        payload = payload_handler(owner)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)

        url = blog_post.get_api_url()
        data = {"title": "Some random title", "content": "more random content"}
        # Anytime you make a request related to your user, you have to pass in a token

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)





'''When testing in this case you create stuff like users,blogposts etc
basically you create instances of things that interact with your app'''