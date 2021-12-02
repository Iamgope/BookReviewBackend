from Base.models import Post
from rest_framework import serializers

class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'BookCoverImage')