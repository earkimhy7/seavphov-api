from django.db import models

#describe the main information of a product/book
class Product(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(max_length=1000, blank=True, null=True)
	genre = models.ForeignKey(
		'products.Genre',
		on_delete=models.SET_NULL,
		null=True,
		related_name='products'
	)
	series = models.ManyToManyField(
		'products.Series',
		through='products.ProductSeries',
		through_fields=('product', 'series')
	)
	authors = models.ManyToManyField(
		'products.Author',
		through='products.ProductAuthor',
		through_fields=('product', 'author')
	)

	def __str__(self):
		return '%s' % (self.title)


#describe the detail of a a book
class Detail(models.Model):
	ISBN = models.CharField(max_length=13, unique=True)
	products = models.ForeignKey(
		'products.Product',
		on_delete=models.CASCADE,
		related_name='product_details'
	)
	pages = models.IntegerField()
	cover_type = models.ForeignKey(
		'products.CoverType',
		on_delete=models.SET_NULL,
		null=True,
		related_name='product_details'
	)
	language = models.ForeignKey(
		'products.Language',
		on_delete=models.CASCADE,
		related_name='product_details'
	)
	publisher = models.ForeignKey(
		'products.Publisher',
		on_delete=models.SET_NULL,
		null=True,
		related_name='product_details'
	)
	publish_date = models.DateTimeField()

	class Meta:
		unique_together = ['products', 'cover_type', 'language', 'publisher', 'publish_date']

	def __str__(self):
		return '%s | %d | %s | %s | %s | %s' % (
			self.ISBN, self.pages, self.cover_type, self.language, self.publisher, self.publish_date)


#the genre of a book (Adventure, Action, etc.)
class Genre(models.Model):
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField(max_length=1000, blank=True, null=True)

	def __str__(self):
		return '%s' % (self.name)


#the series of books
class Series(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(max_length=1000, blank=True, null=True)

	def __str__(self):
		return '%s' % (self.name)


#describe the book series if the book is in any series
class ProductSeries(models.Model):
	product = models.ForeignKey(
		'products.Product',
		on_delete=models.CASCADE,
	)
	series = models.ForeignKey(
		'products.Series',
		on_delete=models.CASCADE,
	)
	number = models.IntegerField()
	

#the information of an author
class Author(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	description = models.TextField(max_length=1000, blank=True, null=True)
	place_of_birth = models.CharField(max_length=255, blank=True, null=True)
	date_of_birth = models.DateTimeField(blank=True, null=True)
	date_of_death = models.DateTimeField(blank=True, null=True)
	website = models.URLField(blank=True, null=True)

	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)


#a book can be written by one or many authors
class ProductAuthor(models.Model):
	product = models.ForeignKey(
		Product,
		on_delete=models.CASCADE,
	)
	author = models.ForeignKey(
		Author,
		on_delete=models.CASCADE,
	)


#show whether the book is paperback or hardcover
class CoverType(models.Model):
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField(max_length=1000, blank=True, null=True)

	def __str__(self):
		return '%s' % (self.name)


#the language of the book
class Language(models.Model):
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField(max_length=1000, blank=True)
	
	def __str__(self):
		return '%s' % (self.name)


#who publishes the book
class Publisher(models.Model):
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField(max_length=1000, blank=True, null=True)
	address = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return '%s' % (self.name)


