from django.urls import path
from Base.views import AddSubscription,AllPosts, PostByCategory, PostListByUser, QuestionList, SinglePost, SubscribedPostsByUser,AddPost, getSingleSubscription, getSubscriptions,PostResponses,PostFinalResponse,MyFinalAnswers,AnswerByQuestion,FinalResponseByPost,getAproovedSubscriptions
from django.views.generic import TemplateView
from Images.views import ImageAPIView
app_name='Base'

urlpatterns = [
    path('', TemplateView.as_view(template_name="base/index.html")),

    path('post/<AssociatedPost>/', QuestionList.as_view(), name='QuestionList'),
    path('postbyCategory/<Category>/', PostByCategory.as_view(), name='PostList'),
    path('singlePost/<int:pk>/', SinglePost.as_view(), name='Single Post'),
    path('MyPosts/', PostListByUser.as_view(), name=' Post By User'),
    path('SubscribedPosts/',SubscribedPostsByUser.as_view(),name="subscried_posts"),
    path('Aprooved_subscribtions/',getAproovedSubscriptions.as_view(),name="MyAproovedSubscriptions"),
    path('AddPost/',AddPost.as_view(),name="Add_Post"),
    path('AddSubscription/',AddSubscription.as_view(),name="Add subscription"),
    path('getSubscriptions/<PostId>/',getSubscriptions.as_view(),name="Get Subscriptions"),
    path('singleSubscription/<int:pk>/', getSingleSubscription.as_view(),name="Single_Subscription"),
    path('AllPosts/',AllPosts.as_view(),name="All_posts"),
    path('PostResponses/',PostResponses.as_view(),name="Post_Response"),
    path('FinalResponse/<AssociatedPost>/',FinalResponseByPost.as_view(),name="Final_Response_By_Post"),
    path('FinalResponse/',PostFinalResponse.as_view(),name="Final_Response"),
   # path('UnpublishedPosts/',UnPublishedPosts.as_view(),name="UnPublished_Posts"),
    path('MyFinalResponses/',MyFinalAnswers.as_view(),name="My Final Answers"),
    path('PostResponses/<questionId>/',AnswerByQuestion.as_view(),name="Answer_By_Question"),
    path('image/<id>/',ImageAPIView.as_view(),name="Images")    

#path('UserAnswer/<QuestionId>/',getUserAnswerByQuestion.as_view(),name="User_Answer")
    


]