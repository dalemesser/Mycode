from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from  .models import Wiwarana
from .forms import WiwaranaForm


def smb(request):
    items = Wiwarana.objects.all()
    form= WiwaranaForm()
    items = items.filter(year =request.GET.get('search'))
    if request.method == "POST":
        form = WiwaranaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("name"))
    context={
        "items":items,
        "form": form,
    }
    return render(request,"smb/main.html",context)

