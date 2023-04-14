import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, View
from django.views.generic.edit import CreateView, UpdateView

from mocker.enums import ResponseType
from mocker.forms import EndpointForm, ServerForm

from .models import Endpoint, Server


class ServerDetailView(LoginRequiredMixin, DetailView):
    model = Server

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["base_url"] = self.request.build_absolute_uri("/")
        return context


class ServerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Server
    form_class = ServerForm
    template_name = "form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update server"
        context["button"] = "Update server"
        return context


class EndpointCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Endpoint
    form_class = EndpointForm
    template_name = "form.html"

    def form_valid(self, form):
        form.instance.server_id = self.kwargs["server_id"]
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new endpoint"
        context["button"] = "Save endpoint"
        return context


class EndpointUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Endpoint
    form_class = EndpointForm
    template_name = "form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update endpoint"
        context["button"] = "Update endpoint"
        return context


class MockerEndpointView(View):
    def get_response(self):
        data = get_object_or_404(
            Endpoint,
            server_id=self.kwargs["server_id"],
            full_path=self.kwargs["fullpath"],
            is_active=True,
        )
        if data.response_type == ResponseType.TEXT:
            return HttpResponse(data.response_body, content_type="text/plain")
        return JsonResponse(json.loads(data.response_body), safe=False)

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return self.get_response()
