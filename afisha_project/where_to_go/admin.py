from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'img', 'position')
    list_editable = ('position', )
    list_filter = ('position',)
