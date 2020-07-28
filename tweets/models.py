import random
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    # Maps to SQL data
    # id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) # tweets no longer have owner upon deletion, still exist in db
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 1020)
        }