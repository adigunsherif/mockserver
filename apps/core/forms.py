from django import forms
from django.forms.widgets import CheckboxInput


class ResponsiveForm(forms.Form):
    """A form to convert all fields to bootstrap form field."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = field.label


class ResponsiveModelForm(ResponsiveForm, forms.ModelForm):
    ...
