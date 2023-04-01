from rest_framework import routers, serializers
from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ['title', 'description', 'thumbnail']