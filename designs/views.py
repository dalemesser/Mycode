from django.shortcuts import render
from .models import Product

def portfolio(request):
    return render(request,"designs/site.html")

def quiz(request):
    return render(request,"designs/quiz.html")

def cards(request):
    return render(request,"designs/cards.html")

def threedcard(request):
    return render(request,"designs/3dcard.html")

def weightconverter(request):
    return render(request,"designs/weightcoverter.html")

def imageslider(request):
    product =Product.objects.all()
    context={
        "products":product
    }
    return render(request,"designs/imageslider.html",context)

def signup(request):
    return render(request,"designs/signup.html")

def timetine(request):
    return render(request,"designs/timeline.html")

def megamenu(request):
    return render(request,"designs/megamenu.html")

def slideblog(request):
    return render(request,"designs/slideblog.html")