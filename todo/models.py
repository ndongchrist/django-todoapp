from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.TextField()
    completed = models.BooleanField(default=False)
    date_Added = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
    