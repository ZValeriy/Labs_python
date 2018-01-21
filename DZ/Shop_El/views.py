from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth import login as auth_login
from .forms import ProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView


def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("list_p")


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    page=''
    if request.META['HTTP_REFERER'] == 'http://127.0.0.1:8000/error/':
        page = 'http://127.0.0.1:8000/'
    else:
        page = request.META['HTTP_REFERER']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return HttpResponseRedirect(page)
    else:
        # Отображение страницы с ошибкой
        return HttpResponseRedirect("/error/")


def signup(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        page = request.META['HTTP_REFERER']
        if form1.is_valid():
            form1.save()
            username = form1.cleaned_data.get('username')
            raw_password = form1.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return HttpResponseRedirect(page)
    else:
        form1 = UserCreationForm()
    return render(request, 'sign_up.html', {'form1': form1})


class ProdCreate(View):
    form3 = ProductForm

    def post(self, request):
        form3 = self.form3(request.POST, request.FILES)
        if form3.is_valid():
            new_prod_id = form3.add_product()
            if new_prod_id:
                context = {'product': Product.objects.get(pk=int(id)),
                           }
                return render(request, '.\pages\product.html', context)
            else:
                return HttpResponseRedirect('/error/')
        else:
            return HttpResponseRedirect('./pages/list')


def list_view(request):
    products = Product.objects.all()
    paginator = Paginator(products, 4)
    form1 = UserCreationForm(request.POST)
    form = AuthenticationForm(request.POST)
    form3 = ProductForm(request.POST, request.FILES)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    context = {'form1': form1, 'form': form, 'products': products, 'form3': form3}
    return render(request, ".\pages\list.html", context)


def base_view(request):
    return render(request, ".\pages\\base.html")


def order(request, id, user_id):
    a = Product.objects.get(pk=id)
    form1 = UserCreationForm(request.POST)
    form = AuthenticationForm(request.POST)
    a.comps.add(int(user_id))
    context = {'form1': form1, 'form': form, 'product': Product.objects.get(pk=int(id)),
               'users': Product.get_username(a)}
    return render(request, '.\pages\product.html', context)


class ErrorView(View):
    template_name = 'error.html'

    def get(self, request):
        data = {'user': request.user,
                'auth': request.user.is_authenticated}
        return render(request, self.template_name, data)


class ProdView(View):
    def get(self, request, id):
        a = Product.objects.get(pk=id)
        form1 = UserCreationForm(request.POST)
        form = AuthenticationForm(request.POST)
        context = {'form1': form1, 'form': form, 'product': Product.objects.get(pk=int(id)), 'users': Product.get_username(a), 'products': Product.objects.all()}
        return render(request, '.\pages\product.html', context)

from .forms import *
from django.http import HttpResponseRedirect, HttpResponse


class ErrorView(View):
    template_name = '.\pages\error.html'

    def get(self, request):
        form1 = UserCreationForm(request.POST)
        form = AuthenticationForm(request.POST)
        context = {'form': form, 'form1': form1}

        return render(request, self.template_name, context)


