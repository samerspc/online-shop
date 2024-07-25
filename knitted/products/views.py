from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from products.models import Product, Basket, Wishlist, Brand, Size
from users.forms import UserLoginForm, UserRegistrationForm
from users.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    products = Product.objects.filter(category__name='shoes')
    loginForm = UserLoginForm()
    registationForm = UserRegistrationForm()
    context = {
        'products': products,
        'loginForm': loginForm,
        'registationForm': registationForm,
    }
    return render(request, 'index.html', context)



def clothes(request):
    context = {
        'products': Product.objects.filter(category__name='clothes'),
    }
    return render(request, 'clothes.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    random_products = Product.objects.order_by('?')[:4]
    context = { 'product': product, 'random_products': random_products, }
    return render(request, 'item.html', context)


@login_required
def baskets(request):
    baskets = Basket.objects.filter(user=request.user)
    total_sum = 0
    for basket in baskets:
        total_sum += basket.sum()
    random_products = Product.objects.order_by('?')[:4]
    context = {
        'baskets': baskets,
        'total_sum': total_sum,
        'random_products': random_products,
    }
    return render(request, 'checkout.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    Basket.objects.create(user=request.user, product=product)
    return HttpResponseRedirect(reverse('basket'))
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER')) stay on the same page

@login_required
def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def wishlist(request):
    context = {
        'wishlist': Wishlist.objects.filter(user=request.user),
    }
    return render(request, 'wishlist.html', context)


# def wishlist_add(request, product_id):
#     product = Product.objects.get(id=product_id)
#     wishlists = Basket.objects.filter(user=request.user, product=product)
#     Wishlist.objects.create(user=request.user, product=product)
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
@login_required
def wishlist_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)

    if created:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# def wishlist_remove(request, id):
#     wishList = Wishlist.objects.get(id=id)
#     wishList.delete()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def wishlist_remove(request, product_id):
    product = Wishlist.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
