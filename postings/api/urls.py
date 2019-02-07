from .views import BlogPostRudView,BlogPostAPIView
from django.conf.urls import url

app_name='postings'


urlpatterns = [
    url(r'^$', BlogPostAPIView.as_view(), name = 'post-create'),
    url(r'^(?P<pk>\d+)/$', BlogPostRudView.as_view(), name = 'post-rud'),

]
