from rest_framework import serializers
from postings.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = BlogPost
        fields = [
            'url',
            'pk',
            'user',
            'title',
            'content',
            'timestamp',
        ]
        read_only_fields = ['user']

        #serialzer converts to JSON
        #Validations for data passed

    def get_url(self, obj):
        return obj.get_api_url()
    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.insance.pk)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used")
        return value



    '''by adding the get api method you will notice that in the api interface you see the url'''