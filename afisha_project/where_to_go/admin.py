from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Place, Image
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline, SortableAdminBase


def get_image_preview_markup(obj, height):
    return  f'<img src="{Image.objects.get(id=obj.id).img.url}" height={height}>'


class ImageInline(SortableStackedInline):
    model = Image
    fields = ('position', 'get_image')
    readonly_fields = ('get_image',)
    extra = 0     #Это определяет количество дополнительных форм, которые набор форм будет отображать в дополнение к исходным формам. По умолчанию 3.

    def get_image(self, obj):  # добавляет в админку отображение картинки
        return mark_safe(get_image_preview_markup(obj, 150))

    get_image.short_description = 'изображение'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('id', 'title',)
    inlines = [     # Добавляет возможность добавить фотографии в другую таблицу из админки этой, связь Foreign Key
        ImageInline,
    ]


@admin.register(Image)
class SortableImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('position', 'get_image', 'get_place_short_title',)   #Показывает эти поля в окне выбора картинки
    readonly_fields = ('get_image',)
    sortable_by = ('place', 'position', )
    list_filter = ('place',)
    ordering = ['position']

    def get_image(self, obj):  # добавляет в админку отображение картинки
        return mark_safe(get_image_preview_markup(obj, 150))

    def get_place_short_title(self, obj):
        return obj.place.get_short_title()

    get_image.short_description = 'изображение'
