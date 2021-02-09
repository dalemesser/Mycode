from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Customer,Products,Order
from .forms import OrderForm,CreatCustomer,RegisterForm
from .filters import OrderFilter
from django.contrib.auth import authenticate,login as dj_login,logout
from django.contrib import messages
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


@unauthenticated_user
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

@unauthenticated_user
def register(request):
    form = RegisterForm()
    context = {
        "form":form,
        "error":form.errors
    }
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name='Customer')
            Customer.objects.create(user=user)
            user.groups.add(group)
            username = form.cleaned_data.get("username")
            messages.success(request,f"Account was created successfully for {username} ")
            return HttpResponseRedirect(reverse("login"))

    return render(request,"web1/register.html", context)

@login_required(login_url="login")
@admin_only
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
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def products(request):
    products = Products.objects.all()
    context ={
        "products":products
    }
    return render(request,'Web1/products.html',context)

@allowed_users(allowed_roles=["admin"])
@login_required(login_url="login")
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


@allowed_users(allowed_roles=["admin"])
@login_required(login_url="login")
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
            product = Products.objects.get(name=form.cleaned_data.get("product"))
            product.qtn -= 1
            product.save()
            print(product.qtn)
            return HttpResponseRedirect(reverse("home"))
    context ={
        "form":form,
        "pending_orders": pending_orders,
        "orders": orders,
        "dilivered_orders": dilivered_orders,
    }
    return render(request,"web1/orderform.html",context)
@allowed_users(allowed_roles=["admin"])
@login_required(login_url="login")
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


@allowed_users(allowed_roles=["admin"])
@login_required(login_url="login")
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


@allowed_users(allowed_roles=["admin"])
@login_required(login_url="login")
def deleteorder(request,id):
    order = Order.objects.get(id=id)
    if request.method == "POST":
        order.delete()
        return HttpResponseRedirect(reverse("home"))
    context = {
            "order":order
        }
    return render(request,"web1/delete.html",context)

@allowed_users(allowed_roles=["admin"])
@login_required(login_url="login")
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

@allowed_users(allowed_roles=["admin"])
@login_required(login_url="login")
def deletecustomer(request,id):
    customer = Customer.objects.get(id=id)
    if request.method == "POST":
        customer.delete()
        return HttpResponseRedirect(reverse("home"))
    context = {
            "customer":customer
        }
    return render(request,"web1/deletecustomer.html",context)



def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
@allowed_users(allowed_roles=["Customer"])
@login_required(login_url="login")
def userpage(request):
    order = request.user.customer.order_set.all()
    orders = order.count()
    pending_orders = order.filter(status="pending").count()
    dilivered_orders = order.filter(status="dilivered").count()
    context = {
        "order":order,
        "orders":orders,
        "pending_orders":pending_orders,
        "dilivered_orders":dilivered_orders
    }
    return render(request,"web1/userpage.html",context)

@allowed_users(allowed_roles=["Customer"])
@login_required(login_url="login")
def account(request):
    user =request.user.customer
    form = CreatCustomer(instance=user)
    if request.method == "POST":
        form = CreatCustomer(request.POST, request.FILES,instance=user)
        if form.is_valid():
            form.save()
    context={
        "form":form
    }
    return render(request,"web1/account.html",context)

