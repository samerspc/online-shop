from django.contrib import admin
from products.models import Brand, Size, Product, ProductSize, Basket, Wishlist, Category

admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(ProductSize)

admin.site.register(Basket)
admin.site.register(Wishlist)

admin.site.register(Category)