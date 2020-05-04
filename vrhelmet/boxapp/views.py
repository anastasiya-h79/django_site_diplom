from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import get_list_or_404

from .models import ProductInOrder, UserInfo, Delivery, MethodPay
from prodapp.views import DateContextMixin


# Create your views here.
# вьюшка для корзины заказа с правами для залогиненного текущего пользователя
class OrderListView(LoginRequiredMixin, ListView, DateContextMixin):
    model = ProductInOrder
    template_name = 'boxapp/order.html'

    def test_func(self):
        return self.request.user

# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.http import require_POST
# from prodapp.models import Helmets
# from .cart import Cart
# from .forms import CartAddProductForm
#
#
# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Helmets, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'],
#                  update_quantity=cd['update'])
#     return redirect('cart:cart_detail')
#
# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Helmets, id=product_id)
#     cart.remove(product)
#     return redirect('cart:cart_detail')
#
# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, 'cart/detail.html', {'cart': cart})

from django.http import JsonResponse
from .models import ProductInBasket


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print (request.POST)
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     is_active=True, defaults={"nmb": nmb})
        if not created:
            print ("not created")
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)

    #common code for 2 cases
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_basket.count()
    return_dict["products_total_nmb"] = products_total_nmb

    return_dict["products"] = list()

    for item in  products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)