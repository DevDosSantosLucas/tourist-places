from django.contrib.auth.models import User
from django.db import models
import uuid

class comment(models.Model):
    #id = models.UUIDField(primary_key=True , default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approved =models.BooleanField(default=False)
   
    def __str__(self):
        return self.user.username
    

