from django.db import models

from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel

CHARFIELD_LONG_LENGTH = 256


@register_setting
class SiteContentSettings(BaseSetting):
    meta_description_default = models.CharField(max_length=CHARFIELD_LONG_LENGTH, blank=True)
    meta_image_default = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldPanel('meta_description_default'),
        ImageChooserPanel('meta_image_default'),
    ]

    class Meta:
        verbose_name = 'Site Content Settings'


class BasePage(Page):
    """Base page to provide basic config for all pages"""
    meta_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    promote_panels = Page.promote_panels + [
        ImageChooserPanel('meta_image'),
    ]

    class Meta:
        abstract = True
