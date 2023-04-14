from django.db import models
from django.urls import reverse

from core.models import TimestampedModel
from mocker.enums import ResponseType
from mocker.status_codes import StatusCodes


class Server(TimestampedModel):
    label = models.CharField("Server Name/Label", max_length=200, unique=True)
    base_path = models.CharField(
        max_length=200, help_text="e.g, api/Products (without the initial and last /)"
    )

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("server-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        endpoints = self.endpoints.all()
        for endpoint in endpoints:
            endpoint.full_path = f"{self.base_path}/{endpoint.endpoint_path}"
            endpoint.save()


class Endpoint(TimestampedModel):
    server = models.ForeignKey(
        Server, on_delete=models.CASCADE, related_name="endpoints"
    )
    endpoint_path = models.CharField(
        max_length=200, help_text="e.g, api/Products (without the initial and last /)"
    )
    status_code = models.IntegerField(
        choices=StatusCodes.choices, default=StatusCodes.HTTP_200_OK
    )
    response_type = models.CharField(
        max_length=100, choices=ResponseType.choices, default=ResponseType.JSON
    )
    response_body = models.TextField()
    full_path = models.TextField()
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("server-detail", kwargs={"pk": self.server.pk})

    def save(self, *args, **kwargs):
        self.full_path = f"{self.server.base_path}/{self.endpoint_path}"
        super().save(*args, **kwargs)
