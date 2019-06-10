from django.db.models import Min, Max
from rest_framework import serializers

from . import models


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'image',
        )
        model = models.Genre


class InventorySerializer(serializers.ModelSerializer):
    condition = serializers.StringRelatedField()

    class Meta:
        fields = (
            'seller',
            'condition',
            'price',
            'quantity',
        )
        model = models.Inventory


class DetailSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=models.Product.objects.all())
    cover_type = serializers.StringRelatedField()
    language = serializers.StringRelatedField()
    publisher = serializers.StringRelatedField()
    min_price = serializers.SerializerMethodField()
    max_price = serializers.SerializerMethodField()
    inventories = InventorySerializer(many=True)

    class Meta:
        fields = (
            'id',
            'ISBN',
            'product',
            'page',
            'cover_type',
            'language',
            'publisher',
            'min_price',
            'max_price',
            'image',
            'inventories',
        )
        model = models.Detail

    @staticmethod
    def get_min_price(obj):
        return obj.inventories.aggregate(Min('price'))

    @staticmethod
    def get_max_price(obj):
        return obj.inventories.aggregate(Max('price'))


class ProductSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()
    authors = serializers.StringRelatedField(many=True)
    details = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='detail-detail',
        queryset=models.Detail.objects.all()
    )

    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'genre',
            'authors',
            'thumbnail',
            'details',
        )
        model = models.Product


class AuthorSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'description',
            'place_of_birth',
            'date_of_birth',
            'date_of_death',
            'website',
            'image',
            'products',
        )
        model = models.Author


# class SeriesSerializer(serializers.ModelSerializer):
#     products = 'ProductSerializer(many=True, read_only=True)'
#
#     class Meta:
#         fields = (
#             'id',
#             'name',
#             'description',
#             'products',
#         )
#         model = models.Series

