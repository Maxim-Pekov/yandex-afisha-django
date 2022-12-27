from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Place, Image
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableStackedInline


class ImageStackedInline(SortableStackedInline):
    model = Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('img', 'get_image', 'position')
    readonly_fields = ('get_image',)
    extra = 0     #Это определяет количество дополнительных форм, которые набор форм будет отображать в дополнение к исходным формам. По умолчанию 3.

    def get_image(self, obj):   #добавляет в админку отображение картинки
        return mark_safe(f'<img src="{Image.objects.get(id=obj.id).img.url}" height="200">')

    get_image.short_description = 'изображение'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    inlines = [     # Добавляет возможность добавить фотографии в другую таблицу из админки этой, связь Foreign Key
        ImageInline,
    ]


@admin.register(Image)
class SortableImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'get_image', 'position')
    readonly_fields = ('get_image',)
    list_editable = ('position', )
    ordering = ['my_order']

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" height="200">')

    get_image.short_description = 'изображение'
