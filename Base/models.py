from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField
from django.utils import timezone
from datetime import datetime, timedelta
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


options = (
    ('closed', 'Closed'),
    ('notClosed', 'NotClosed')
)


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='notClosed')

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=False)
    BookCoverImage =  CloudinaryField('image')
    published = models.DateTimeField(default=timezone.now)

    status = models.CharField(
        max_length=10, choices=options, default='notClosed')

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=User)
    authorName = models.CharField(max_length=100)
    isPublished = models.BooleanField(default=False)
    PostData = models.FileField(upload_to="uploads/PostData", default=0)

    objects = models.Manager()
    postobjects = PostObjects()

    def __str__(self):
        return self.title


class Question(models.Model):
    AssociatedPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, default="subjective")
    question = models.TextField(null=False)
    option1 = models.TextField(null=True)
    option2 = models.TextField(null=True)
    option3 = models.TextField(null=True)
    option4 = models.TextField(null=True)

    def __str__(self):
        return self.question


class Response(models.Model):
    Response = models.TextField(null=False)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, default="subjective")

    def __str__(self):
        return self.question

    class Meta:
        unique_together = ('question', 'User',)


class FinalResponse(models.Model):
    Response = models.TextField(null=False)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    AssociatedPost = models.ForeignKey(Post, on_delete=CASCADE)
    username = models.CharField(max_length=100)
    isLiked = models.IntegerField(default=0)

    class Meta:
        unique_together = ('AssociatedPost', 'User')

    def __str__(self):
        return self.question.question


class SubscribedPosts(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    Age = models.IntegerField()
    ReviewedPosts = models.IntegerField()
    Sex = models.CharField(max_length=50)
    AssociatedPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    BookCoverImage = models.CharField(max_length=500)
    isAprooved = BooleanField(default=False)
    reviewed = BooleanField(default=False)

    class Meta:
        unique_together = ('AssociatedPost', 'User',)

    def __str__(self):
        return self.AssociatedPost.title
