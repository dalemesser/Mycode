from django.urls import path
from . import  views
urlpatterns = [
    path("",views.portfolio,name="portforlio"),
    path("quiz",views.quiz,name="quiz"),
    path("weightconverter",views.weightconverter,name="converter"),
    path("cards",views.cards,name="cards"),
    path("3dcards",views.threedcard,name="cards")
]