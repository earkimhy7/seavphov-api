from django.db.models import Min, Max
from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()
    authors = serializers.StringRelatedField(many=True)
    # series = serializers.StringRelatedField(many=True)
    details = 'DetailSerializer(many=True, read_only=True)'

    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'genre',
            'authors',
            # 'series',
            'thumbnail',
            'details',
        )
        model = models.Product


class DetailSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    cover_type = serializers.StringRelatedField()
    language = serializers.StringRelatedField()
    publisher = serializers.StringRelatedField()

    class Meta:
        fields = (
            'id',
            'ISBN',
            'product',
            'pages',
            'cover_type',
            'language',
            'publisher',
            'publish_date',
            'image',
        )
        model = models.Detail


class GenreSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'image',
            'products',
        )
        model = models.Genre


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

