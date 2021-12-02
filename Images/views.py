from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from Images.serializers import ImagesSerializer
from Images.custom_renderers import JPEGRenderer, PNGRenderer
from rest_framework.response import Response
from rest_framework import generics
from Base.models import Post
# Create your views here.
class ImageAPIView(generics.RetrieveAPIView):
    serializer_class=ImagesSerializer
    queryset = Post.objects.filter(id=1)
    renderer_classes = [JPEGRenderer]

    def get(self, request, *args, **kwargs):
        renderer_classes = [PNGRenderer]
        queryset = Post.objects.get(id=self.kwargs['id']).BookCoverImage
        data = queryset
        return Response(data, content_type='image/jpg')