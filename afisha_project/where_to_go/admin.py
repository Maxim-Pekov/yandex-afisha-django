from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Place, Image
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableStackedInline, SortableAdminBase


def get_image_preview_markup(obj, height):
    return f'<img src="{Image.objects.get(id=obj.id).img.url}" ' \
           f'height={height}>'


class ImageInline(SortableStackedInline):
    model = Image
    fields = ('position', 'get_image',)
    readonly_fields = ('get_image',)
    extra = 0

    def get_image(self, obj):
        return mark_safe(get_image_preview_markup(obj, 150))

    get_image.short_description = 'изображение'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('id', 'title',)
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class SortableImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('position', 'get_image', 'get_place_short_title',)
    readonly_fields = ('get_image',)
    sortable_by = ('place', 'position', )
    list_filter = ('place',)
    ordering = ['position']

    def get_image(self, obj):  # добавляет в админку отображение картинки
        return mark_safe(get_image_preview_markup(obj, 150))

    def get_place_short_title(self, obj):
        return obj.place.get_short_title()

    get_image.short_description = 'изображение'
