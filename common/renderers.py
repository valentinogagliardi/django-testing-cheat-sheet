from django.forms.renderers import TemplatesSetting


class FormRenderer(TemplatesSetting):
    field_template_name = "common/field.html"