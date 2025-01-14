from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ...


class TimestampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        related_query_name="%(app_label)s_%(class)ss",
    )

    class Meta:
        abstract = True
