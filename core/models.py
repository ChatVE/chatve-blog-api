from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

#Main Post Model

class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    slug = AutoSlugField(populate_from="title", unique=True, primary_key=True)
    date_posted = models.DateField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name="comment")
    comment = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + "||||" + self.post.title



# Create your models here.
