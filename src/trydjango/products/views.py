from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import Product

from .forms import ProductForm, RawProductForm
# Create your views here.
def product_list_view(request):
    qurryset = Product.objects.all() #list of object
    context ={
        "object_list" : qurryset
    }
    return render(request,"products/product_list.html",context)

def dynamic_lookup_view(request,my_id):
    #obj = Product.objects.get(id=id)
    #obj = get_object_or_404(Product,id=id)
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object" : obj
    }
    return render(request,"products/product_detail.html",context)

def render_initail_data(request):

    #obj = Product.objects.get(id=1)
    obj = Product.objects.get(id=1)
    print(obj)
    initial_data = {
        'title' : obj.title,
        'description' : obj.description
    }
    form = RawProductForm(request.POST or None,initial=initial_data)
    #form = RawProductForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request,"products/product_create.html",context)

#def product_create_view(request):
#    form = RawProductForm()
#    if request.method == "POST":
#        form = RawProductForm(request.POST)
#        if form.is_valid():
#            print(form.cleaned_data)
#            Product.objects.create(**form.cleaned_data)
#        else:
#            print(form.errors)
#    context = {
#        'form' : form
#    }
#    return render(request,"products/product_create.html",context)


#def product_create_view(request):
#    #print(request.GET)
#    #print(request.POST)
#    if request.method == "POST":
#        my_new_title = request.POST.get("title")
#        print(my_new_title)
#    context = {}
#    return render(request,"products/product_create.html",context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form' : form
    }
    return render(request,"products/product_create.html",context)

#def product_detail_view(request):
#    obj = Product.objects.get(id=1)
#    context = {
#        'object' : obj
#    }
#    return render(request,"products/product_detail.html",context)
