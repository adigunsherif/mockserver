from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from mocker.forms import ServerForm


class DashboardView(LoginRequiredMixin, View):
    template_name = "dashboard.html"

    def get(self, request):
        context = {"servers": request.user.servers.all(), "form": ServerForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = ServerForm(request.POST)
        if form.is_valid():
            form.instance.created_by = request.user
            instance = form.save()
            return redirect(instance)
        context = {"servers": request.user.servers.all(), "form": form}
        return render(request, self.template_name, context)
