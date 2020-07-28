from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .form import CreateForm

# Create your views here.
def display_products(request):
    AllProducts = Product.objects.all()

    context={ 
        "AllProducts":AllProducts }
    return render(request,'index.html',context)

def create_product(request):
    create_form = CreateForm()
    if request.method == 'POST':
        create_form=CreateForm(request.POST)
        if create_form.is_valid():
            aux = create_form.save(commit=False)
            aux.save()
            return redirect('display')
    context ={
        "create_form" :create_form
    }
    return render(request,"add.html",context)

def update_product(request,p_id):
    ProductToUpdate = get_object_or_404(Product,id=p_id) 
    context ={
        "ProductToUpdate":ProductToUpdate
    }
    if request.method =="PUT":
        Product.objects.filter(id = p_id).update(request.PUT)
        return redirect('display')
    return render(request,"update.html",context)

def delete_product(request,p_id):
   product_to_delete = get_object_or_404(Product,id=p_id) 
   product_to_delete.delete()
   return redirect('display')