from rest_framework import serializers
from sellers.models import Seller, SellerType, Image


# ****************************** Manage Seller Merchant Information ******************************#
# Update Merchant

# ******************************  Manage Seller Contact Information *******************************#
# Update Contact Info
class SellerContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = (
            'pk',
            'phone'
        )


# ******************************  Manage Seller info and Upgrade ****************************#
# Update Profile Pic
class SellerUpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = (
            'pk',
            'profile_picture'
        )


# Update Cover Picture
class SellerUpdateCoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = (
            'pk',
            'cover'
        )


# Seller Manage Address Information
class SellerManageAddressInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = (
            'house_number',
            'street_number',
            'village',
            'communes',
            'district',
            'province_city',
            'countries',
            'postal_code'
        )


# Image
class SellerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'image',
            'seller'
        )


#  Seller Type
class SellerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerType
        fields = (
            'pk',
            'name',
            'description'
        )

    def validate_name(self, value):
        qs = SellerType.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This Type of Seller already have !")
        return value


# Seller
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = (
            'pk',
            'name',
            'description',
            'email',
            'phone',
            'house_number',
            'street_number',
            'village',
            'communes',
            'district',
            'province_city',
            'countries',
            'postal_code',
            'created_at',
            'updated_at',
            'seller_type'
        )

    def validate_email(self, value):
        qs = Seller.objects.filter(email__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This email has already been used !")
        return value

# B Yong Code
# def create(self, validated_data):
#     print(self.context.get('request').data)
#     print(validated_data)
#     seller_type = SellerType.objects.get(pk=validated_data.get('seller_type'))
#     validated_data['seller_type'] = seller_type
#     print(validated_data)
#     print(seller_type)
#     instance = Seller.objects.create(**validated_data)
#     return instance

# def to_internal_value(self, data):
#     ret = super().to_internal_value(data)
#     ret.items['seller_type']= int(ret.items['seller_type'])
#     return ret
