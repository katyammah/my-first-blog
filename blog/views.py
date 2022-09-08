from django.shortcuts import render
from .models import Post, Order
from django.utils import timezone
from .forms import OrderForm
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, 'blog/post_list.html', {'posts': posts})


# Create your views here.


def catalog(request):
    # clothes = Post.objects.filter(title__contains = "Жакет").order_by("published_date")
    return render(request, 'blog/catalog.html')



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