from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
  description = models.TextField()
  is_complete = models.BooleanField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.description
