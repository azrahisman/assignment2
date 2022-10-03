from django.db import models
from django.contrib.auth.models import User

class ItemTodolist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=50)
    description = models.TextField()