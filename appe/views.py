from django.shortcuts import render, redirect
from  .models import Customer_details,Vendor_details,Add_newproduct



# Create your views here.
# def showIndex(request):
#     return render(request,"index.html")
def customersignup(request):
    if request.method == "POST":
        uname = request.POST.get("Username")
        email = request.POST.get("Email")
        mobileno = request.POST.get("Mobileno")
        password = request.POST.get("Password")

        one = uname[-2]
        two = mobileno[-3]
        three = uname[2]
        four = password[-4]
        five = email[5]
        six = password[-1]

        otp = four + one + str(two) + three + five + six

        message = sendEcommerceSMS(mobileno, otp)
        import json
        d1 = json.loads(message)
        if d1['return']:
            qs = Customer_details(USERNAME=uname, PASSWORD=password, EMAIL=email, MOBILENO=mobileno,OTP=otp)
            qs.save()
            return render(request, "Registered_Customer_OtpVerify.html")

def check_customerotp(request):
    if request.method == "POST":
        otp = request.POST.get("Otp")
        print(otp)
        qs = Customer_details.objects.filter(OTP=otp)
        if qs:
            return render(request, "logins.html", {"msg": "Registered Successfully"})
        else:
            return render(request, "Registered_Customer_OtpVerify.html", {"msg": "Invalid Otp"})


def customerlogin(request):
    email = request.POST.get("Email")
    password = request.POST.get("Password")
    qs = Customer_details.objects.filter(EMAIL=email,PASSWORD=password)
    if qs:
        qs1 = Customer_details.objects.filter(EMAIL=email)
        request.session['cname'] = qs1[0].USERNAME
        return render(request,"customerdashboard.html",{"data":qs,"message":"Successfully Login"})
    else:
        return render(request,"login_Customer.html",{"msg":"Invalid Customer"})

def vendorsignup(request):
    if request.method == "POST":
        uname = request.POST.get("Username")
        email = request.POST.get("Email")
        mobileno = request.POST.get("Mobileno")
        password = request.POST.get("Password")

        one = uname[0]
        two = mobileno[-5]
        three = uname[-2]
        four = password[3]
        five = email[2]
        six = password[-1]


        otp = four + one + str(two) + three + five + six

        message = sendEcommerceSMS(mobileno,otp)
        import json
        d1 = json.loads(message)
        if d1['return']:
            Vendor_details(USERNAME=uname,EMAIL=email,MOBILENO=mobileno,PASSWORD=password,OTP=otp).save()
            return render(request, "Registered_Vendor_OtpVerify.html")

def sendEcommerceSMS(mobileno,otp):
    import requests

    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=Hello welcome to Ecommerce........!Your OTP Is......"+otp+"&language=english&route=p&numbers="+mobileno
    headers = {
        'authorization': "76eLvonl6aTGNEBYhmaaTX6xfIGNUuZdFwosHBTpHZvDKDPDF9ollY55mc7L",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.text


def check_vendorotp(request):
    if request.method == "POST":
        otp = request.POST.get("Otp")
        print(otp)
        qs = Vendor_details.objects.filter(OTP=otp)
        if qs:
            return render(request, "logins.html", {"msg": "Registered Successfully"})
        else:
            return render(request, "Registered_Vendor_OtpVerify.html", {"msg": "Invalid Otp"})


def vendorlogin(request):
    email = request.POST.get("Email")
    password = request.POST.get("Password")
    qs = Vendor_details.objects.filter(EMAIL=email,PASSWORD=password)
    if qs:
        qs1 = Vendor_details.objects.filter(EMAIL=email)
        request.session['vname'] = qs1[0].USERNAME
        return render(request,"dashboard.html",{"data":qs,"message":"Successfully Login"})
    else:
        return render(request,"login_Vendor.html",{"msg":"Invalid Vendor"})


def clogout(request):
    del request.session['cname']
    return redirect('clogin')


def vlogout(request):
    del request.session['vname']
    return redirect('vlogin')


def addnewproduct(request):
    if request.method == "POST":
        type = request.POST.get("type")
        categories = request.POST.get("categories")
        categorytype = request.POST.get("categorytype")
        size = request.POST.get("size")
        quantity = request.POST.get("quantity")
        name = request.POST.get("name")
        image = request.FILES['image']
        price = request.POST.get("price")
        description = request.POST.get("description")
        Add_newproduct(TYPE=type,CATEGORIES=categories,CATEGORIETYPE=categorytype,SIZE=size,QUANTITY=quantity,
                        NAME=name,IMAGE=image,PRICE=price,DESCRIPTION=description).save()
        qs = Add_newproduct.objects.all()
        return render(request, "addnew_Product.html", {"msg": "Product added Successfully", "data": qs})


