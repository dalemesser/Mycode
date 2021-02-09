from django.urls import path
from . import  views
urlpatterns = [
    path("",views.portfolio,name="portforlio"),
    path("quiz",views.quiz,name="quiz"),
    path("weightconverter",views.weightconverter,name="converter"),
    path("cards",views.cards,name="cards"),
    path("3dcards",views.threedcard,name="cards"),
    path("imageslider",views.imageslider,name="imageslider"),
    path("signup",views.signup,name="signup"),
    path("timeline",views.timetine,name="timeline"),
    path("megamenu",views.megamenu,name="megamenu"),
    path("slideblog",views.slideblog,name="slideblog")
]