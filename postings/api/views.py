#generic

from rest_framework import generics
from postings.models import BlogPost
from .serializers import BlogPostSerializer
class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView): #DetailView CreateView FormView --> generics
    lookup_field = 'pk' #url mapping : url(r'?P<pk>\d+')
    serializer_class =  BlogPostSerializer
    #queryset = BlogPost.objects.all()
#Overiding the guery set method
    def get_queryset(self):
        return BlogPost.objects.all()
#Since its a retrieve view you can also override the lookup field method
    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return BlogPost.objects.get(pk=pk)