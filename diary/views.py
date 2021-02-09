from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect,HttpResponse
from  .models import Items,ToDoItems
from .forms import DiaryForm,ToDoForm,RegisterForm
from django.contrib import messages
import datetime
from django.contrib.auth import authenticate,logout,login as dj_login
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required


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
            username = form.cleaned_data.get("username")
            messages.success(request,f"Account was created successfully for {username} ")
            return HttpResponseRedirect(reverse("login"))

    return render(request,"dairy/register.html", context)

@unauthenticated_user
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)
        if user is not None:
            dj_login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.info(request,"Username or Password Is Incorrect")
    return render(request,"web1/login.html")


#main template view which shows the todo items for the day and the dairy items specific for the searched date.

@login_required(login_url="login")
def show_dairy(request):
    items_todo = ToDoItems.objects.filter(date=datetime.datetime.now())
    items = Items.objects.filter(date=request.GET.get('search'))
    context={
        "items":items,
        "items_to":items_todo
    }
    return render(request,"dairy/main.html",context)

#main template view which shows the
#todo items by the specific date

def show_todo(request):
    items_todo = ToDoItems.objects.filter(date=request.GET.get('search'))
    context={
        "items_to":items_todo
    }
    return render(request,"dairy/main.html",context)

#show the dairy form and save the date in to the database

def dairy(request):
    form = DiaryForm()
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    context = {
        "form": form,
    }
    return render(request, "dairy/dairyform.html", context)


#show the todo form and save the data into the database
def todo(request):
    todoform = ToDoForm()
    if request.method == "POST":
        todoform = ToDoForm(request.POST)
        if todoform.is_valid():
            todoform.save()
            return HttpResponseRedirect(reverse("index"))
    context = {
        "form": todoform,
    }
    return render(request, "dairy/todoform.html", context)





def update(request,id):
    item = Items.objects.get(id=id)
    form = DiaryForm(instance=item)
    item.delete
    if request.method == "POST":
        form =  DiaryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    context={
        "item" :item,
        "form":form
    }
    return render(request,"dairy/main.html",context)


def delete(request,id):
    item = Items.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponse("Invalid format")



