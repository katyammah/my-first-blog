from django.shortcuts import render
from .models import Post, Product
from django.utils import timezone
from .forms import OrderForm, ProductForm
from django.shortcuts import redirect


def main_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, 'blog/main.html', {'posts': posts})


def catalog(request):
    products = Product.objects.order_by('-created_date')
    if request.method == "POST":
        form = ProductForm(request.POST)
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
