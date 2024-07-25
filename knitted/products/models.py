from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    materials = models.TextField(blank=True, null=True)
    first_image = models.ImageField(upload_to='products/', blank=True, null=True)
    second_image = models.ImageField(upload_to='products/', blank=True, null=True)
    third_image = models.ImageField(upload_to='products/', blank=True, null=True)
    fourth_image = models.ImageField(upload_to='products/', blank=True, null=True)
    fifth_image = models.ImageField(upload_to='products/', blank=True, null=True)
    sizes = models.ManyToManyField('Size', through='ProductSize')

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.size


class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('product', 'size')

    def __str__(self):
        return f"{self.product.name} - {self.size.size}"


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Корзина {self.user.username}"

    def sum(self):
        return self.product.price


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Избранное {self.user.username}"


















