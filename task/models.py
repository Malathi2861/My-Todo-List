from django.db import models


class Todo(models.Model):
    content = models.CharField(max_length=250)

    def __str__(self):
        return self.content

