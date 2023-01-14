from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Place, Image
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableStackedInline, SortableAdminBase


def get_image_preview_markup(image):
    return mark_safe(f'<img src="{image.img.url}" height=200>')


class ImageInline(SortableStackedInline):
    model = Image
    fields = ('position', get_image_preview_markup,)
    readonly_fields = (get_image_preview_markup,)
    extra = 0

    get_image_preview_markup.short_description = 'изображение'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('id', 'title',)
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class SortableImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        'position',
        get_image_preview_markup,
        'get_place_short_title',
    )
    readonly_fields = (get_image_preview_markup,)
    sortable_by = ('place', 'position',)
    list_filter = ('place',)
    ordering = ['position']

    def get_place_short_title(self, image):
        title = image.place.title.strip()
        if len(title) < 20:
            return title
        elif '«' in title:
            title_in_quotes = title.replace('»', '').split('«')[1]
            short_title = ' '.join(title_in_quotes.split()[:4]) + '...'
            return short_title
        return ' '.join(title.split()[:4]) + '...'

    get_image_preview_markup.short_description = 'изображение'
    get_place_short_title.short_description = 'короткое название'
