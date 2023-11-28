from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect

def login(request):
    if request.method=="POST":
        un= request.POST.get("unm")
        ps= request.POST.get("pas")
        print(ps)
        if Login.objects.filter(username=un,password=ps):
            obj=Login.objects.filter(username=un,password=ps)
            print("rrrrrrrrrrrrr",obj)
            tp=""
            for l in obj:
                tp=l.type
                uid=l.login_id
                if tp=="customer":
                    request.session["uid"]=uid
                    return HttpResponseRedirect('/customer/customer_home/')
                elif tp=="seller":
                    request.session["uid"] = uid
                    return HttpResponseRedirect('/seller/seller_home/')
                elif tp=="subseller":
                    request.session["uid"] = uid
                    return HttpResponseRedirect('/subseller/subseller_home/')
        else:
            obje = "Incorrect username or password!!!"
            context = {
                'inv': obje,
            }
            return render(request, 'login/login.html', context)
    return render(request, 'login/login.html')
