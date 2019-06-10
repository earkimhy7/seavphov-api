from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    house_number = models.TextField(max_length=25, null=True, blank=True)
    street_number = models.TextField(max_length=25, null=True, blank=True)
    village = models.TextField(max_length=50, null=True, blank=True)
    communes = models.TextField(max_length=50, null=True, blank=True)
    district = models.TextField(max_length=50, null=True, blank=True)
    province_city = models.TextField(max_length=50, null=True, blank=True)
    countries = models.TextField(max_length=50, null=True, blank=True)
    postal_code = models.TextField(max_length=25, null=True, blank=True)
    seller_type = models.ForeignKey('SellerType', on_delete=models.CASCADE,
                                    related_name='sellers')
    profile_picture = models.ImageField(upload_to='pictures/sellers/')
    cover = models.ImageField(upload_to='pictures/sellers/')
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SellerType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return '%s' % (self.name)


class Verification(models.Model):
    seller = models.OneToOneField('Seller', on_delete=models.CASCADE,
                                  related_name='verification_of')
    date = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE)
    image = models.ImageField('pictures/sellers/images/')
