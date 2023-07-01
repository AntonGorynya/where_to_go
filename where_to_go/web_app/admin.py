from django.contrib import admin
from .models import Place, Image

admin.site.register(Image)

class ImageInline(admin.TabularInline):
    model = Image
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


