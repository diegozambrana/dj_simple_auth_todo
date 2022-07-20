from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Todo(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE);
    todo_json = models.TextField(default="[]");

    def __str__(self) -> str:
        return self.user.username