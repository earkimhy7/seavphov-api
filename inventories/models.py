from django.db import models


# this is the function to upload image
def upload_image(instance, filename):
    return '/'.join(['inventories', str(instance.name), filename])


# describe the main information of a product/book
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, blank=True, null=True)
    genre = models.ForeignKey(
        'Genre',
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )
    authors = models.ManyToManyField(
        'Author',
        through='ProductAuthor',
        through_fields=('product', 'author'),
        related_name='product_list',
    )
    # series = models.ManyToManyField(
    #     'Series',
    #     through='ProductSeries',
    #     through_fields=('product', 'series'),
    #     related_name='product_list',
    # )
    thumbnail = models.ImageField(upload_to=upload_image, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.title


# describe the detail of a a book
class Detail(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    products = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='details'
    )
    pages = models.IntegerField()
    cover_type = models.ForeignKey(
        'CoverType',
        on_delete=models.SET_NULL,
        null=True,
        related_name='details'
    )
    language = models.ForeignKey(
        'Language',
        on_delete=models.CASCADE,
        related_name='details'
    )
    publisher = models.ForeignKey(
        'Publisher',
        on_delete=models.SET_NULL,
        null=True,
        related_name='details'
    )
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['products', 'cover_type', 'language', 'publisher', 'publish_date']

    def __str__(self):
        return '%s | %d | %s | %s | %s | %s' % (
            self.ISBN, self.pages, self.cover_type, self.language, self.publisher, self.publish_date)


# the genre of a book (Adventure, Action, etc.)
class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.name


# the series of books
# class Series(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(max_length=1000, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return '%s' % self.name


# describe the book series if the book is in any series
# class ProductSeries(models.Model):
#     product = models.ForeignKey(
#         'Product',
#         on_delete=models.CASCADE,
#     )
#     series = models.ForeignKey(
#         'Series',
#         on_delete=models.CASCADE,
#     )
#     number = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# the information of an author
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, blank=True, null=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    date_of_death = models.DateTimeField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['first_name', 'last_name', 'place_of_birth', 'date_of_birth', 'date_of_death']

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


# a book can be written by one or many authors
class ProductAuthor(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# show whether the book is paperback or hardcover
class CoverType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.name


# the language of the book
class Language(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.name


# who publishes the book
class Publisher(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.name
