from django.urls import path
from . import views

urlpatterns = [
    path("",views.show_dairy,name="index"),
    path("<int:id>/update",views.update,name="update"),
    path("<int:id>/delete",views.delete,name="delete")
]