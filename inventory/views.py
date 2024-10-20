from django.shortcuts import render, get_object_or_404, redirect
from  .forms import ProductForm
from .models import Product

def create_or_update_product(request, product_id=None):

    if product_id:
        product = get_object_or_404( Product, id=product_id)
    else:
        product = None

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('inventory:create')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'inventory/create_update_product.html', {'form':form})


def list_products(request):
    products = Product.objects.all()[:19]
    return render(request,'inventory/products.html', {'products': products} )