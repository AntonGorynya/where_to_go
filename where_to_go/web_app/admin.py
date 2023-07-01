from django.contrib import admin
from django.utils.html import mark_safe
from .models import Place, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = [
        'preview'
    ]
    def preview(self, obj):
        return mark_safe('<img src="{url}" style="max-height:200px">'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
        )
        )

class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = [
        'preview'
    ]

    def preview(self, obj):
        return mark_safe('<img src="{url}" style="max-height:200px">'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
        )
        )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


