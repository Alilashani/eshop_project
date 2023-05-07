from django.contrib import admin
from . import models


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category', 'is_active']
    list_display = ['title', 'price', 'is_active', 'is_delete']
    list_editable = ['price', 'is_active']
    search_fields = ['title', 'price']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('brand',)


@admin.register(models.ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'is_active']
    list_editable = ['is_active']
    search_fields = ['title']


class ProductVisitAdmin(admin.ModelAdmin):
    list_display = ['product', 'ip', 'user']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTag)
# admin.site.register(models.ProductBrand, ProductBrandAdmin)
admin.site.register(models.ProductVisit, ProductVisitAdmin)
admin.site.register(models.ProductGallery)
