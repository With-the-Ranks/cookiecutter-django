from django.db import models

from {{ cookiecutter.project_slug }}.core.models import BasePage, CommonHeroPageFields, ContentStreamField

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(BasePage, CommonHeroPageFields, ContentStreamField):

    content_panels = BasePage.content_panels + CommonHeroPageFields.content_panels + ContentStreamField.content_stream_field_panels
