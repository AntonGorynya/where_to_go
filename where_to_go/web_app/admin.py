from django.contrib import admin
from .models import Place, Image


#@admin.register(Place)
admin.site.register(Place)
admin.site.register(Image)

