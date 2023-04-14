from django.urls import path, re_path

from . import views

urlpatterns = [
    path("server/<int:pk>/", views.ServerDetailView.as_view(), name="server-detail"),
    path(
        "server/<int:pk>/update/",
        views.ServerUpdateView.as_view(),
        name="server-update",
    ),
    path(
        "endpoint/<int:server_id>/add/",
        views.EndpointCreateView.as_view(),
        name="endpoint-create",
    ),
    path(
        "endpoint/<int:pk>/update/",
        views.EndpointUpdateView.as_view(),
        name="endpoint-update",
    ),
    re_path(
        r"^server(?P<server_id>\d+)/(?P<fullpath>[\w\/\-.@]+)$",
        views.MockerEndpointView.as_view(),
    ),
]
