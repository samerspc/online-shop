"""
URL configuration for knitted project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products import views as viewProduct
from users import views as viewUsers
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', viewProduct.index, name='index'),
    path('clothes/', viewProduct.clothes, name='clothes'),

    path('admin/', admin.site.urls),

    path('product/<int:pk>/', viewProduct.product_detail, name='product_detail'),

    path('login/', viewUsers.login, name='login'),
    path('registration/', viewUsers.registration, name='registration'),
    path('profile/', viewUsers.profile, name='profile'),
    path('logout/', viewUsers.logout, name='logout'),

    path('basket/', viewProduct.baskets, name='basket'),
    path('basketadd/<int:product_id>/', viewProduct.basket_add, name='basketadd'),
    path('basketremove/<int:id>/', viewProduct.basket_remove, name='basketremove'),

    path('wishlist/', viewProduct.wishlist, name='wishlist'),
    path('wishlistadd/<int:product_id>/', viewProduct.wishlist_add, name='wishlistadd'),
    path('wishlistremove/<int:product_id>/', viewProduct.wishlist_remove, name='wishlistremove'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)