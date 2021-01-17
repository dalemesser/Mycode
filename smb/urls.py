from django.urls import path
from . import views

urlpatterns = [
    path("",views.smb,name="name")
]