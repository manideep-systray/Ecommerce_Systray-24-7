"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, ListView
from appe.models import Add_newproduct
from appe import views
from ecommerce import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"),name='index'),
    path('login/', TemplateView.as_view(template_name="logins.html")),
    path('newcustomersignup/', TemplateView.as_view(template_name="registered_Customer.html")),
    path('customersignup/', views.customersignup),
    path('check_customerotp/', views.check_customerotp),
    path('newcustomerlogin/', TemplateView.as_view(template_name="login_Customer.html"),name='clogin'),
    path('customerlogin/',views.customerlogin),
    path('newvendorsignup/', TemplateView.as_view(template_name="registered_Vendor.html")),
    path('vendorsignup/', views.vendorsignup),
    path('check_vendorotp/', views.check_vendorotp),
    path('newvendorlogin/',TemplateView.as_view(template_name="login_Vendor.html"),name='vlogin'),
    path('vendorlogin/', views.vendorlogin),
    # path('index/', TemplateView.as_view(template_name="index.html")),
    # path('products/', TemplateView.as_view(template_name="products.html")),
    path('products/', ListView.as_view(template_name="products.html",model=Add_newproduct,queryset=Add_newproduct.objects.filter(TYPE="women"))),
    path('products1/', ListView.as_view(template_name="products1.html",model=Add_newproduct,queryset=Add_newproduct.objects.filter(TYPE="men"))),
    path('products2/', ListView.as_view(template_name="products2.html",model=Add_newproduct,queryset=Add_newproduct.objects.filter(TYPE="kid"))),
    # path('products1/', TemplateView.as_view(template_name="products1.html")),
    # path('products2/', TemplateView.as_view(template_name="products2.html")),
    path('mail/', TemplateView.as_view(template_name="mail.html")),
    path('dashboard/', TemplateView.as_view(template_name="dashboard.html")),
    path('customerdashboard/', TemplateView.as_view(template_name="customerdashboard.html")),
    path('yourproducts/', TemplateView.as_view(template_name="your_Products.html")),
    path('previousproducts/', TemplateView.as_view(template_name="previous_Products.html")),
    path('addnewproducts/', TemplateView.as_view(template_name="addnew_Product.html")),
    path('addnewproduct/',views.addnewproduct),
    path('inventory/', TemplateView.as_view(template_name="inventory.html")),
    path('soldproducts/', TemplateView.as_view(template_name="sold_Product.html")),
    path('returnproducts/', TemplateView.as_view(template_name="return_Product.html")),
    path('youraddresses/', TemplateView.as_view(template_name="your_Address.html")),
    path('addnewaddress/', TemplateView.as_view(template_name="addnew_Address.html")),
    path('manageaddress/', TemplateView.as_view(template_name="manage_Address.html")),
    path('updateaddress/', TemplateView.as_view(template_name="update_Address.html")),
    path('changepwd/', TemplateView.as_view(template_name="changepassword.html")),


    path('clogout/',views.clogout),
    path('vlogout/',views.vlogout),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)