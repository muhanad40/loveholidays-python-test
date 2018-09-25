from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
  description = models.TextField()
  is_complete = models.BooleanField()

  def __str__(self):
    return self.description
