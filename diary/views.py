from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect,HttpResponse
from  .models import Items
from .forms import DiaryForm


def show_dairy(request):
    items = Items.objects.all()
    form= DiaryForm()
    items = items.filter(date =request.GET.get('search'))
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    context={
        "items":items,
        "form": form,
    }
    return render(request,"dairy/main.html",context)

def update(request,id):
    item = Items.objects.get(id=id)
    form = DiaryForm(instance=item)
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
