from django.shortcuts import render
from rating.models import Rating
from payment.models import Payment
from product_order.models import ProductOrder
from cart.models import Cart
import datetime
from login.models import Login
from products.models import Product


def customer_add_rating(request,idd):
    uid = request.session["uid"]
    owner_id = Login.objects.get(login_id=uid)

    order_id = Payment.objects.get(payment_id=idd)
    cart_id = ProductOrder.objects.get(order_id=order_id.order_id,order_status='accepted')
    product_id = Cart.objects.get(cart_id=cart_id.cart_id)
    owner_id = Product.objects.get(product_id=product_id.product_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        obj = Rating()
        obj.product_type = product_id.product_type
        obj.product_id = product_id.product_id
        obj.date = datetime.date.today()
        obj.customer_id = owner_id.owner_id
        obj.owner_id = owner_id.owner_id
        obj.rating = rating
        obj.save()
    return render(request, 'rating/customer_add_rating.html')


def seller_view_ratings(request):
    uid = request.session["uid"]
    owner_id = Login.objects.get(login_id=uid)

    ratings = Rating.objects.filter(owner_id=owner_id.user_id,product_type='new')
    context = {
        'rating':ratings
    }
    return render(request, 'rating/seller_view_ratings.html',context)


def subseller_view_ratings(request):
    uid = request.session["uid"]
    owner_id = Login.objects.get(login_id=uid)

    ratings = Rating.objects.filter(owner_id=owner_id.user_id,product_type='old')
    context = {
        'rating':ratings
    }
    return render(request, 'rating/subseller_view_ratings.html',context)


