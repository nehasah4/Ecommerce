from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    slug = models.CharField(max_length=500,unique=True)

    def __str__(self):
        return self.name



class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=500,unique=True)

    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    url = models.URLField(max_length=500,blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    rank = models.IntegerField()

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


STATUS = (('Active','Active'),('Inactive','Inactive'))
LABELS = (('new', 'new'),('hot', 'hot'), ('sale','sale'),('','default'))


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    specification = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    slug = models.CharField(max_length=300,unique=True)
    status = models.CharField(max_length=50, choices=STATUS)
    labels = models.CharField(max_length=50, choices=LABELS)

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    post = models.CharField(max_length=500)
    comment = models.TextField()
    star = models.IntegerField()

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProductReview(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    date = models.DateField(auto_now_add=True)
    star = models.IntegerField()
    comment = models.TextField()
    slug = models.CharField(max_length=500)

    def __str__(self):
        return self.name



