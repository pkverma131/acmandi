from django.contrib import admin

from .models import Product, ProductHighlight, ProductMedia, ProductLink, \
    Specification, SpecificationType, Brand


class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'title', 'description')
    fields = ('brand', 'title', 'description')


admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductHighlight)
admin.site.register(ProductMedia)
admin.site.register(ProductLink)
admin.site.register(SpecificationType)
admin.site.register(Specification)
