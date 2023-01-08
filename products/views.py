from django.shortcuts import render, redirect

from products.models import Product
from products.forms import ProductForm

import os
from django.conf import settings

def list(request):
    products = Product.objects.all()
    return render(request, "products/list.html", {'products':products})

def new(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            print("No es válido")
            print(form.errors)
    else:
        form = ProductForm()
    return render(request, "products/new2.html", {'form':form})

def details(request, id):
    p = Product.objects.get(pk=id)
    return render(request, "products/details.html", {'product':p})

def fav(request):
    fav = request.session.get('fav', None)
    if fav:
        fav = set(fav.split('.'))
    fav_prod = Product.objects.filter(id__in=fav)
    print(fav_prod)
    return render(request, "products/fav.html", {'fav':fav_prod})

def unlike(request, id):
    p = Product.objects.get(pk=id)
    fav = request.session.get('fav', None)
    if fav:
        fav = fav.split('.')
        fav.remove(str(p.id))
    fav = '.'.join(fav)
    print(fav)
    request.session['fav'] = fav
    return redirect('fav_products')

def like(request, id):
    p = Product.objects.get(pk=id)
    fav = request.session.get('fav', None)
    if not fav:
        request.session['fav'] = str(p.id)
    else:
        request.session['fav'] += "." + str(p.id)
    return redirect('products')




def delete(request, id):
    p = Product.objects.get(pk=id)
    if p.image:
        os.remove(os.path.join(settings.MEDIA_ROOT, p.image.name))
    p.delete()
    return redirect("products")
