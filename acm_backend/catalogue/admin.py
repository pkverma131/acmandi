from django.contrib import admin

from .models import Product, ProductHighlight, ProductMedia, ProductLink, \
    Specification, SpecificationType, Brand, MarketPlace, PerHourEnergyConsumed,\
    ProductCategory, ProductToProductCategory


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'company', 'origin_country',
                    'manufacture_country', 'support_contact', 'support_email', 'address')
    fields = ('name', 'code', 'company', 'origin_country',
              'manufacture_country', 'support_contact', 'support_email', 'address')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'title', 'description', 'thumbnail')
    fields = ('brand', 'title', 'description', 'thumbnail')


class ProductHighlightAdmin(admin.ModelAdmin):
    list_display = ('highlight', 'type')
    fields = ('highlight', 'type')


class ProductMediaAdmin(admin.ModelAdmin):
    list_display = ('product', 'is_thumbnail', 'media_file')
    fields = ('product', 'is_thumbnail', 'media_file')


class ProductLinkAdmin(admin.ModelAdmin):
    list_display = ('product', 'marketplace', 'link', 'mrp', 'discount', 'sales_price')
    fields = ('product', 'marketplace', 'link', 'mrp', 'discount', 'sales_price')


class SpecificationTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'description')
    fields = ('type', 'description')


class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('specification_type', 'label', 'value')
    fields = ('specification_type', 'label', 'value')


class MarketPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'website')
    fields = ('name', 'logo', 'website')


class PerHourEnergyConsumedAdmin(admin.ModelAdmin):
    list_display = ('product', 'unit_consumed')
    fields = ('product', 'unit_consumed')


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'thumbnail')
    fields = ('name', 'description', 'thumbnail')


class ProductToProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_category')
    fields = ('product','product_category')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductHighlight, ProductHighlightAdmin)
admin.site.register(ProductMedia, ProductMediaAdmin)
admin.site.register(ProductLink, ProductLinkAdmin)
admin.site.register(SpecificationType, SpecificationTypeAdmin)
admin.site.register(Specification, SpecificationAdmin)
admin.site.register(MarketPlace, MarketPlaceAdmin)
admin.site.register(PerHourEnergyConsumed, PerHourEnergyConsumedAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductToProductCategory, ProductToProductCategoryAdmin)
