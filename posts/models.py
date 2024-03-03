from django.db import models
from accounts.models import User


class Post(models.Model):
    author = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField("tags.Tag", through="tags.TagPostSet", related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def truncated_description(self):
        return self.description[:300]
