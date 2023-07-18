from django.contrib import admin
from django.utils.html import mark_safe, format_html
from .models import Place, Image
from adminsortable2.admin import SortableAdminMixin, SortableTabularInline


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = [
        'preview'
    ]
    list_display = ['place', 'order', 'preview']

    def preview(self, obj):
        return format_html('<img src="{url}" style="max-height:200px">', url=obj.image.url)


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = [
        'preview'
    ]

    def preview(self, obj):
        return format_html('<img src="{url}" style="max-height:200px">', url=obj.image.url)


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
