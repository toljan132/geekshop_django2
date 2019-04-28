from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from mainapp.models import Product
from .models import Basket
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse

@login_required
def basket(request):
    basket = request.user.basket.all()
    context = {
        'basket_items': basket,
    }
    return render(request, 'basketapp/basket.html', context)


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))

    product = get_object_or_404(Product, pk=pk)
    basket = request.user.basket.filter(product=pk).first()
    if basket:
        basket.quantity += 1
        basket.save()
    else:
        new_basket = Basket(user=request.user, product=product)
        new_basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = request.user.basket.filter(pk=pk).first()
    if basket:
        if basket.quantity > 1:
            basket.quantity -= 1
            basket.save()
        else:
            basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        print(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))
            
        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()
            
        basket_items = Basket.objects.filter(user=request.user).\
                                      order_by('product__category')
        
        content = {
            'basket_items': basket_items,
        }
        
        result = render_to_string('basketapp/includes/inc_basket_list.html',\
                                   content)
        
        return JsonResponse({'result': result})
