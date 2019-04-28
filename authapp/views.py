from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib import auth
from django.urls import reverse
from basketapp.models import Basket

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def login(request):
    title = 'Login'

    login_form = ShopUserLoginForm(data=request.POST or None)

    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('index'))

    context = {
        'title': title,
        'login_form': login_form,
        'next': next
    }

    return render(request, 'authapp/login.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    title = 'Registration'

    register_form = ShopUserRegisterForm(request.POST, request.FILES)
    if request.method == 'POST':

        if register_form.is_valid():
            new_user = register_form.save()
            auth.login(request, new_user)
            return HttpResponseRedirect(reverse('index'))

    context = {'title': title, 'form': register_form}
    return render(request, 'authapp/register.html', context)


def edit(request):
    basket = get_basket(request.user)

    title = 'Edit'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    context = {'title': title,
               'form': edit_form,
               'basket': basket}

    return render(request, 'authapp/register.html', context)