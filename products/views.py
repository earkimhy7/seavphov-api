from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from . import models
from . import serializers


class ProductViewSet(viewsets.ModelViewSet):
	queryset = models.Product.objects.all()
	serializer_class = serializers.ProductSerializer

	@detail_route(methods=['post'])
	def authors(self, request, pk=None):
		product = self.get_object()
		serializer = serializers.AuthorSerializer(product.authors.all(), many=True)
		return Response(serializers.data)

	@detail_route(methods=['post'])
	def details(self, request, pk=None):
		product = self.get_object()
		serializer = serializers.DetailSerializer(product.details.all(), many=True)
		return Response(serializer.data)




class GenreViewSet(viewsets.ModelViewSet):
	queryset = models.Genre.objects.all()
	serializer_class = serializers.GenreSerializer


class DetailViewSet(viewsets.ModelViewSet):
	queryset = models.Detail.objects.all()
	serializer_class = serializers.DetailSerializer


class AuthorViewSet(viewsets.ModelViewSet):
	queryset = models.Author.objects.all()
	serializer_class = serializers.AuthorSerializer