from django.db import models


class Labels(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
