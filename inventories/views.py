from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from . import models
from . import serializers


class ProductViewSet(viewsets.ModelViewSet):
	queryset = models.Product.objects.all()
	serializer_class = serializers.ProductSerializer
	filter_fields = ('title', 'genre__name',)

	@detail_route(methods=['get'])
	def details(self, request, pk=None):
		product = self.get_object()
		serializer = serializers.DetailSerializer(product.details.all(), many=True)
		return Response(serializer.data)


class GenreViewSet(viewsets.ModelViewSet):
	queryset = models.Genre.objects.all()
	serializer_class = serializers.GenreSerializer
	filter_fields = ('name',)

	@detail_route(methods=['get'])
	def products(self, request, pk=None):
		genre = self.get_object()
		serializer = serializers.ProductSerializer(genre.products.all(), many=True)
		return Response(serializer.data)


class DetailViewSet(viewsets.ModelViewSet):
	queryset = models.Detail.objects.all()
	serializer_class = serializers.DetailSerializer
	filter_fields = ('product', 'cover_type', 'publisher', 'publish_date')


class AuthorViewSet(viewsets.ModelViewSet):
	queryset = models.Author.objects.all()
	serializer_class = serializers.AuthorSerializer
