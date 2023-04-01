from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Post, Product, Basket
from django.utils import timezone
from .forms import OrderForm, ProductForm, UserCreateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordResetView
from django.views.generic import DetailView


def main_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, 'blog/main.html', {'posts': posts})


def catalog(request):
    products = Product.objects.order_by('-created_date')

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('catalog')

    else:
        form = ProductForm()
    return render(request, 'blog/catalog.html', {'products': products, 'form': form})


def customer_data(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user
            contact.save()
            return redirect('customer_data_ok')
    else:
        form = OrderForm()
    return render(request, 'blog/customer_data.html', {'form': form})


def customer_data_ok(request):
    return render(request, 'blog/customer_data_ok.html')


def contacts(request):
    return render(request, 'blog/contacts.html')


def registration(request):
    user = request.user
    products = Product.objects.order_by('-created_date')
    if user.is_authenticated:
        basketofuser = Basket.objects.filter(user=request.user)
        endsum = 0
        for basket in basketofuser:
            endsum += basket.product.price

        return render(request, 'blog/registration.html', {'products': products,
                                                          'basketofuser': basketofuser,
                                                          'endsum': endsum
                                                          })
    else:
        return render(request, 'blog/registration.html', {'products': products})


def register(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreateForm()
    return render(request, 'registration/register.html', {'form': form})


class MyPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'


class DetailOfProduct(DetailView):
    model = Product
    template_name = 'blog/info_product.html'



def basket_add(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    if user.is_authenticated:
        baskets = Basket.objects.filter(user=user, product=product)
        if not baskets.exists():
            Basket.objects.create(user=user, product=product, quantity=1)
            return redirect('registration')
        else:
            return redirect('registration')


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def checkout(request):
    return render(request, 'blog/checkout.html')