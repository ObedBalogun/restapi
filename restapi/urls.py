from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/postings/', include('postings.api.urls', namespace='api-postings')),
]

