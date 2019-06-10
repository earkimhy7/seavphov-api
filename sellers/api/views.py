from django.db.models import Q
from rest_framework import generics, mixins
from sellers.models import Seller, SellerType, Image
from .serializers import SellerSerializer, SellerTypeSerializer, SellerImageSerializer, \
    SellerManageAddressInfoSerializer, SellerUpdateCoverSerializer, SellerUpdateProfileSerializer, \
    SellerContactSerializer
from rest_framework.parsers import FormParser, MultiPartParser


#####  Seller_API  #####
# List_user
class SellerAPIViewAll(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = SellerSerializer
    parser_classes = (FormParser, MultiPartParser)
    queryset = Seller.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Retrieve
class SellerRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = SellerSerializer

    def get_queryset(self):
        return Seller.objects.all()


#####  Seller Type API  ######
# List seller type
class SellerTypeAPIViewAll(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = SellerTypeSerializer
    parser_classes = (FormParser, MultiPartParser)
    queryset = SellerType.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Retrieve
class SellerTypeRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = SellerTypeSerializer

    def get_queryset(self):
        return SellerType.objects.all()


#####  Seller Image API  ######
# List seller image
class SellerImageAPIViewAll(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = SellerImageSerializer
    parser_classes = (FormParser, MultiPartParser)
    queryset = Image.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Retrieve
class SellerImageRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = SellerImageSerializer

    def get_queryset(self):
        return Image.objects.all()


#####  Seller Manage Address Info #####
class SellerManageAddressInfoRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = SellerManageAddressInfoSerializer

    def get_queryset(self):
        return Seller.objects.all()


##### Seller Update Profile ######
class SellerUpdateProfileRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = SellerUpdateProfileSerializer

    def get_queryset(self):
        return Seller.objects.all()


##### Seller Update Cover ######
class SellerUpdateCoverRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = SellerUpdateCoverSerializer

    def get_queryset(self):
        return Seller.objects.all()


class SellerUpadteContactInfoRudView(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = SellerContactSerializer

    def get_queryset(self):
        return Seller.objects.all()
