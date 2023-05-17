from django.contrib import admin
from .models import Category, Plant

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price','size','stock', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

    def delete_selected(self, request, queryset):
        queryset.delete()

    delete_selected.short_description = 'Delete selected'

admin.site.register(Plant, PlantAdmin)


