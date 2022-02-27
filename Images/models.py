from django.db import models

# Create your models here.

from django.db import models
from cloudinary.models import CloudinaryField
from Base.models import Post


class photos(models.Model):
    # title field
    AssociatedPost = models.ForeignKey(
        Post, on_delete=models.CASCADE, )
    # image field
    image = CloudinaryField('image')

    def __str__(self):
        return self.AssociatedPost
