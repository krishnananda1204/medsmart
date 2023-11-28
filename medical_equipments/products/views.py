from django.shortcuts import render
from products.models import Product
from stock.models import Stock
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect

def customer_search_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        category = request.POST.get("category")
        product_type = request.POST.get("type")
        obj = Product.objects.filter(name__icontains=name,category=category,product_type=product_type)
        obb=Stock.objects.all()
        context={
            'search':obj,
            'stocks':obb
        }
        return render(request, 'products/customer_search_product.html',context)
    return render(request, 'products/customer_search_product.html')


def seller_manage_products(request):
    obj=Product.objects.filter(product_type="new")
    obb=Stock.objects.all()
    context={
        'items':obj,
        'stocks':obb
    }
    return render(request, 'products/seller_manage_products.html',context)


def seller_reg_products(request):
    if request.method == "POST":
        obj=Product()
        obj.name = request.POST.get("name")
        obj.description = request.POST.get("description")
        obj.price = request.POST.get("price")
        obj.mfg_date = request.POST.get("mfg_date")
        obj.category = request.POST.get("category")
        obj.product_type = "new"

        img=request.FILES['image']
        ff=FileSystemStorage()
        filename=ff.save(img.name,img)
        obj.image=img.name

        obj.save()

        obb = Stock()
        obb.stock = request.POST.get("stock")
        obb.product_id = obj.product_id
        obb.save()
    return render(request, 'products/seller_reg_products.html')


def subseller_manage_products(request):
    obj=Product.objects.filter(product_type="old")
    obb=Stock.objects.all()
    context={
        'items':obj,
        'stocks':obb
    }
    return render(request, 'products/subseller_manage_products.html',context)


def subseller_reg_products(request):
    if request.method == "POST":
        obj=Product()
        obj.name = request.POST.get("name")
        obj.description = request.POST.get("description")
        obj.price = request.POST.get("price")
        obj.mfg_date = request.POST.get("mfg_date")
        obj.category = request.POST.get("category")
        obj.product_type = "old"

        img=request.FILES['image']
        ff=FileSystemStorage()
        filename=ff.save(img.name,img)
        obj.image=img.name

        obj.save()

        obb = Stock()
        obb.stock = request.POST.get("stock")
        obb.product_id = obj.product_id
        obb.save()
    return render(request, 'products/subseller_reg_products.html')


def subseller_update_product_details(request,idd):
    obb=Product.objects.filter(product_id=idd)
    context={
        'items':obb
    }
    print(obb)
    if request.method == "POST":
        obj=Product.objects.get(product_id=idd)
        obj.name = request.POST.get("name")
        obj.description = request.POST.get("description")
        obj.price = request.POST.get("price")
        obj.mfg_date = request.POST.get("mfg_date")
        obj.category = request.POST.get("category")


        img=request.FILES['image']
        ff=FileSystemStorage()
        filename=ff.save(img.name,img)
        obj.image=img.name
        obj.save()
        return HttpResponseRedirect('/products/subseller_manage_products/')
    return render(request,'products/subseller_update_pro_details.html',context)


def subseller_update_stock(request,idd):
    obj=Stock.objects.filter(product_id=idd)
    context={
        'items':obj
    }
    if request.method == "POST":
        obb = Stock.objects.get(product_id=idd)
        obb.stock = request.POST.get("stock")
        obb.save()
        return HttpResponseRedirect('/products/subseller_manage_products/')
    return render(request,'products/subseller_update_stock.html',context)


def subseller_delete_product(request,idd):
    obb=Product.objects.get(product_id=idd)
    obb.delete()

    obj=Stock.objects.get(product_id=idd)
    obj.delete()
    return HttpResponseRedirect('/products/subseller_manage_products/')


def seller_update_product_details(request,idd):
    obb=Product.objects.filter(product_id=idd)
    context={
        'items':obb
    }
    # print(obb)
    if request.method == "POST":
        obj=Product.objects.get(product_id=idd)
        obj.name = request.POST.get("name")
        obj.description = request.POST.get("description")
        obj.price = request.POST.get("price")
        obj.mfg_date = request.POST.get("mfg_date")
        obj.category = request.POST.get("category")


        img=request.FILES['image']
        ff=FileSystemStorage()
        filename=ff.save(img.name,img)
        obj.image=img.name
        obj.save()
        return HttpResponseRedirect('/products/seller_manage_products/')
    return render(request,'products/seller_update_pro_details.html',context)


def seller_update_stock(request,idd):
    obj=Stock.objects.filter(product_id=idd)
    context={
        'items':obj
    }
    if request.method == "POST":
        obb = Stock.objects.get(product_id=idd)
        obb.stock = request.POST.get("stock")
        obb.save()
        return HttpResponseRedirect('/products/seller_manage_products/')
    return render(request,'products/seller_update_stock.html',context)


def seller_delete_product(request,idd):
    obb=Product.objects.get(product_id=idd)
    obb.delete()

    obj=Stock.objects.get(product_id=idd)
    obj.delete()
    return HttpResponseRedirect('/products/seller_manage_products/')
