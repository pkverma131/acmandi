from django.conf import settings
from django.db import models


class BaseTimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseUserTrackedModel(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   default=1, related_name='created_by_%(class)s_related')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name='updated_by_%(class)s_related', null=True, blank=True)

    class Meta:
        abstract = True


class AuditModelMixin(BaseTimestampedModel, BaseUserTrackedModel):

    class Meta:
        abstract = True


class Brand(AuditModelMixin):
    logo = models.ImageField(upload_to='brands/logo/', default=None)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    origin_country = models.CharField(max_length=50)
    manufacture_country = models.CharField(max_length=50)
    support_contact = models.CharField(max_length=50)
    support_email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


class Product(AuditModelMixin):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to='products/thumbnail/', default=None)


class ProductMedia(AuditModelMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_thumbnail = models.BooleanField()
    media_file = models.ImageField(upload_to='products/image/', default=None)


class SpecificationType(AuditModelMixin):
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class Specification(AuditModelMixin):
    specification_type = models.ForeignKey(SpecificationType, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    value = models.CharField(max_length=100)


class ProductHighlight(AuditModelMixin):
    highlight = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=(('1', 'TITLE_TAG'), ('2', 'FEATURE')))


class ProductToProductHighlight(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    highlight = models.ForeignKey(ProductHighlight, on_delete=models.CASCADE)


class ProductToSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE)


class MarketPlace(AuditModelMixin):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='marketplaces/logo/')
    website = models.CharField(max_length=100)


class ProductLink(AuditModelMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(MarketPlace, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)
    mrp = models.FloatField()
    discount = models.FloatField()
    sales_price = models.FloatField()


class PerHourEnergyConsumed(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_consumed = models.FloatField()


class ProductCategory(AuditModelMixin):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='product_category/thumbnail/')


class ProductToProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

