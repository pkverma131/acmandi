from django.db import models
from catalogue.models import AuditModelMixin


class TileFilter(AuditModelMixin):
    filter_key = models.CharField(max_length=20)
    filter_value = models.CharField(max_length=20)


class TileCategory(AuditModelMixin):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def tile(self):
        return Tile.objects.filter(tile_category=self.id).values()


class Tile(AuditModelMixin):
    tile_category = models.ForeignKey(TileCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='tiles/thumbnail/', default=None)

    def filter(self):
        return TileToTileFilter.objects.filter(tile=self.id).values()


class TileToTileFilter(models.Model):
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)
    tile_filter = models.ForeignKey(TileFilter, on_delete=models.CASCADE)