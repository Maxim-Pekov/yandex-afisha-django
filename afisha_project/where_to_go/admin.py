from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Place, Image


@admin.register(Place)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


@admin.register(Image)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'img',)
