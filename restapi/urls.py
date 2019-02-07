from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo_list/', include('todo_list.urls')),
    path('api/todo_list/', include('todo_list.api.urls')),
]

