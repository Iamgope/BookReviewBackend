from rest_framework import serializers
from Base.models import *


class GetQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'question', 'type', 'option1', 'option2',
                  'option3', 'option4', 'AssociatedPost')
        model = Question


class GetPostsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'category', 'title', 'excerpt', 'BookCoverImage',
                  'published', 'status', 'author', 'authorName', 'isPublished', 'PostData')
        model = Post


class SubscribedPostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'User', 'AssociatedPost', 'isAprooved', 'Age',
                  'Sex', 'BookCoverImage', 'title', 'username', 'ReviewedPosts','reviewed')
        model = SubscribedPosts


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id', 'User', 'Response', 'question', 'type', 'username')
        model = Response
class FinalResponseSerializer(serializers.ModelSerializer):
   class Meta:
      fields=('id','User','Response','isLiked','username','AssociatedPost')
      model=FinalResponse

class PictureSerialiser(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Post
        fields = ('BookCoverImage')
    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)