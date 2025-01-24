import json

from django import forms
from django.utils.html import escape
from django.utils.safestring import mark_safe

from apps.core.forms import ResponsiveModelForm

from .models import Endpoint, Server


class AceEditorWidget(forms.Textarea):
    class Media:
        js = (
            "https://cdn.jsdelivr.net/npm/ace-builds@latest/src-noconflict/ace.min.js",
        )

    def render(self, name, value, attrs=None, renderer=None):
        if attrs is None:
            attrs = {}
        attrs["hidden"] = "hidden"  # Hide the original textarea
        textarea = super().render(name, value, attrs, renderer)

        editor_id = attrs.get("id", f"id_{name}")
        ace_div_id = f"ace_{editor_id}"
        ace_div = (
            f'<div id="{ace_div_id}" style="height: 300px; width: 100%;">{value}</div>'
        )
        script = f"""
        <script>
            document.addEventListener("DOMContentLoaded", function() {{
                if (typeof ace === 'undefined') {{
                    console.error("Ace Editor is not loaded.");
                    return;
                }}
                var editor = ace.edit("{ace_div_id}");
                editor.setTheme("ace/theme/vibrant_ink");
                editor.session.setMode("ace/mode/json");
                editor.getSession().on('change', function() {{
                    document.getElementById("{editor_id}").value = editor.getValue();
                }});
            }});
        </script>
        """
        return mark_safe(textarea + ace_div + script)


class ServerForm(ResponsiveModelForm):
    class Meta:
        model = Server
        exclude = ("created_by",)


class EndpointForm(ResponsiveModelForm):
    class Meta:
        model = Endpoint
        fields = (
            "endpoint_path",
            "status_code",
            "response_type",
            "response_body",
            "python_code",
            "is_active",
        )
        widgets = {"response_body": AceEditorWidget()}
