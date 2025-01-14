from django.db.models import IntegerChoices, TextChoices


class ResponseType(TextChoices):
    JSON = "application/json"
    TEXT = "text/plain"
