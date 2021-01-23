from django.shortcuts import render

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