from django.conf import settings
from django.db import models


class Tasks(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)

    status = models.ForeignKey('statuses.Status', on_delete=models.PROTECT)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='authored_tasks',
    )

    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='executed_tasks',
        null=True,
        blank=True,
    )

    labels = models.ManyToManyField('labels.Labels')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
