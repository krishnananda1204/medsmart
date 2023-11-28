from django.shortcuts import render
from cart.models import Cart
from products.models import Product
from stock.models import Stock
from product_order.models import ProductOrder
import datetime
from django.http import HttpResponseRedirect


def add_to_cart(request,idd):
    uid = request.session["uid"]
    obj=Product.objects.get(product_id=idd)
    if request.method == "POST":
        q = request.POST.get("quantity")

        st = Stock.objects.get(product_id=idd)
        if int(st.stock) > int(q):
            obb=Cart()
            obb.product_type = obj.product_type
            obb.product_id = obj.product_id
            obb.quatity = request.POST.get("quantity")

            total_amount = int(obj.price)*int(q)
            obb.total = total_amount
            obb.user_id = uid
            obb.date = datetime.date.today()
            obb.cart_status = 'pending'
            obb.save()

            new_stock = int(st.stock)-int(q)
            st.stock = new_stock
            st.save()
        else:
            obje = "Out of stock..!!!"
            context = {
                'inv': obje,
            }
            return render(request, 'cart/add_to_cart.html',context)
    return render(request, 'cart/add_to_cart.html')


def view_cart(request):
    uid = request.session["uid"]
    obj = Cart.objects.filter(user_id=uid,cart_status='pending')
    print(obj)
    context = {
        'data': obj
    }
    return render(request,'cart/view_cart.html',context)

def customer_place_order(request,idd):
    uid = request.session["uid"]
    data = Cart.objects.get(cart_id=idd)
    uid = request.session["uid"]
    obj = ProductOrder()
    obj.date = datetime.date.today()
    obj.time = datetime.datetime.now().strftime("%H:%M:%S")
    obj.cart_id=idd
    obj.user_id = uid
    obj.total_amount = data.total
    obj.order_status = 'pending'
    obj.save()

    data.cart_status = 'order placed'
    data.save()
    return HttpResponseRedirect('/cart/view_cart/')