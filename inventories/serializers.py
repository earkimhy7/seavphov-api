from django.db.models import Min, Max
from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()
    authors = serializers.StringRelatedField(many=True)

    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'genre',
            'authors',
            'thumbnail',
        )
        model = models.Product


class DetailSerializer(serializers.ModelSerializer):
    cover_type = serializers.StringRelatedField()
    language = serializers.StringRelatedField()
    publisher = serializers.StringRelatedField()

    class Meta:
        fields = (
            'id',
            'ISBN',
            'page',
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

