from django import forms

from core.forms import ResponsiveModelForm

from .models import Endpoint, Server


class ServerForm(ResponsiveModelForm):
    class Meta:
        model = Server
        exclude = ("created_by",)


class EndpointForm(ResponsiveModelForm):
    class Meta:
        model = Endpoint
        fields = ("endpoint_path", "status_code", "response_type", "response_body")
