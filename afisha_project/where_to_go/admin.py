from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('img', 'get_image', 'position')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{Image.objects.get(id=obj.id).img.url}" height="200">')

    get_image.short_description = 'изображение'


@admin.register(Place)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_image', 'position')
    readonly_fields = ('get_image',)
    list_editable = ('position', )

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" height="200">')

    get_image.short_description = 'изображение'
