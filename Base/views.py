from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, serializers
from Base.models import Post, Response
from Base.serializers import GetQuestionsSerializer
from Base.models import Question
from Base.models import Category
from Base.serializers import GetPostsSerializer
from Base.models import SubscribedPosts
from Base.serializers import SubscribedPostSerializer
from Base.serializers import ResponseSerializer
from Base.serializers import FinalResponseSerializer
from Base.models import FinalResponse


class QuestionList(generics.ListCreateAPIView):
   # queryset=Question.objects.all()
    # ssociatedPost
    serializer_class = GetQuestionsSerializer

    def get_queryset(self):
        PostId = self.kwargs['AssociatedPost']
        return Question.objects.filter(AssociatedPost=PostId)


class PostByCategory(generics.ListAPIView):

    serializer_class = GetPostsSerializer

    def get_queryset(self):
        CategoryId = self.kwargs['Category']
        return Post.objects.filter(category=CategoryId,isPublished=False)


class SinglePost(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = GetPostsSerializer




class AllPosts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = GetPostsSerializer


class PostListByUser(generics.ListAPIView):
    serializer_class = GetPostsSerializer

    def get_queryset(self):

        userId = self.request.user.id
        # print(userId)
       # print('BUN', userId)
        return Post.objects.filter(author=userId)


class SubscribedPostsByUser(generics.ListAPIView):
    serializer_class = SubscribedPostSerializer

    def get_queryset(self):

        userId = self.request.user.id
        # print(userId)
        #print('BUN', userId)
        return SubscribedPosts.objects.filter(User=userId)


class AddPost(generics.CreateAPIView):
    serializer_class = GetPostsSerializer


class AddSubscription(generics.CreateAPIView):
    serializer_class = SubscribedPostSerializer


class getSubscriptions(generics.ListAPIView):
    serializer_class = SubscribedPostSerializer

    def get_queryset(self):
        PostId = self.kwargs['PostId']
        return SubscribedPosts.objects.filter(AssociatedPost=PostId)


class getAproovedSubscriptions(generics.ListAPIView):
    serializer_class = SubscribedPostSerializer

    def get_queryset(self):
        #PostId = self.kwargs['PostId']
        UserId=self.request.user.id
        return SubscribedPosts.objects.filter( isAprooved=True,User=UserId)


class getSingleSubscription(generics.RetrieveUpdateAPIView):
    queryset = SubscribedPosts.objects.all()

    serializer_class = SubscribedPostSerializer


class PostResponses(generics.ListCreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer


class PostFinalResponse(generics.ListCreateAPIView):
    queryset = FinalResponse.objects.all()
    serializer_class = FinalResponseSerializer

class FinalResponseByPost(generics.ListCreateAPIView):
    #queryset = FinalResponse.objects.all()
    serializer_class = FinalResponseSerializer
    def get_queryset(self):
        PostId=self.kwargs['AssociatedPost']
        return FinalResponse.objects.filter(AssociatedPost=PostId)

class MyFinalAnswers(generics.ListAPIView):
    serializer_class = FinalResponseSerializer

    def get_queryset(self):
        return FinalResponse.objects.filter(User=self.request.user.id)


class AnswerByQuestion(generics.ListAPIView):
    serializer_class = ResponseSerializer

    def get_queryset(self):
        QuestionId = self.kwargs['questionId']
        return Response.objects.filter(question=QuestionId)
