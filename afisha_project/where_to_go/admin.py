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

    def get_image(self, obj):
        return mark_safe(get_image_preview_markup(obj, 150))

    @staticmethod
    def get_place_short_title(obj):
        title = obj.place.title.strip()
        if len(title) < 20:
            return title
        elif '«' in title:
            title_in_quotes = title.replace('»', '').split('«')[1]
            short_title = ' '.join(title_in_quotes.split()[:4]) + '...'
            return short_title
        return ' '.join(title.split()[:4]) + '...'

    get_image.short_description = 'изображение'
