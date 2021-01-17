from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Customer,Products,Order
from .forms import OrderForm,CreatCustomer,RegisterForm
from .filters import OrderFilter
from django.contrib.auth import authenticate,login as dj_login,logout
from django.contrib import messages

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)
        if user is not None:
            dj_login(request,user)
            return HttpResponseRedirect(reverse("home"))
        else:
            messages.info(request,"Username or Password Is Incorrect")
    return render(request,"web1/login.html")

def register(request):
    form = RegisterForm()
    context = {
        "form":form,
        "error":form.errors
    }
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request,f"Account was created successfully for {user} ")
            return HttpResponseRedirect(reverse("login"))

    return render(request,"web1/register.html", context)

def home(request):
    customers = Customer.objects.all()
    order_items = Order.objects.all()
    orders= order_items.count()
    pending_orders = Order.objects.filter(status="pending").count()
    dilivered_orders = Order.objects.filter(status="dilivered").count()
    context={
        "order_item": order_items,
        "pending_orders":pending_orders,
        "orders":orders,
        "dilivered_orders":dilivered_orders,
        "customers":customers
    }
    return render(request,'Web1/dashbord.html',context)

def products(request):
    products = Products.objects.all()
    context ={
        "products":products
    }
    return render(request,'Web1/products.html',context)

def customers(request,id):
    customer = Customer.objects.get(id=id)
    order = customer.order_set.all()
    orders_count = order.count()
    myFilter = OrderFilter(request.GET,queryset=order)
    order = myFilter.qs
    context = {
        "customer":customer,
        "order":order,
        "orders_count":orders_count,
        "myFilter":myFilter
    }
    return render(request,'Web1/customers.html',context)

def create_order(request):
    form = OrderForm()
    order_items = Order.objects.all()
    orders = order_items.count()
    pending_orders = Order.objects.filter(status="pending").count()
    dilivered_orders = Order.objects.filter(status="dilivered").count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    context ={
        "form":form,
        "pending_orders": pending_orders,
        "orders": orders,
        "dilivered_orders": dilivered_orders,
    }
    return render(request,"web1/orderform.html",context)

def create_customer(request):
    form = CreatCustomer()
    if request.method == "POST":
        form = CreatCustomer(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    context={
        "form":form
    }
    return render(request,"web1/createcustomer.html",context)

def update_order(request,id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    context={
        "form":form
    }
    return render(request,"web1/orderform.html",context)

def deleteorder(request,id):
    order = Order.objects.get(id=id)
    if request.method == "POST":
        order.delete()
        return HttpResponseRedirect(reverse("home"))
    context = {
            "order":order
        }
    return render(request,"web1/delete.html",context)

def update_customer(request,id):
    customer = Customer.objects.get(id = id)
    form = CreatCustomer(instance=customer)
    if request.method == "POST":
        form = CreatCustomer(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    context = {
        "form": form
    }
    return render(request, "web1/createcustomer.html", context)

def deletecustomer(request,id):
    customer = Customer.objects.get(id=id)
    if request.method == "POST":
        customer.delete()
        return HttpResponseRedirect(reverse("home"))
    context = {
            "customer":customer
        }
    return render(request,"web1/deletecustomer.html",context)

def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))