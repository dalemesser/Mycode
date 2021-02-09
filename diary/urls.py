from django.urls import path
from . import views

urlpatterns = [
    path("",views.show_dairy,name="index"),
    path("form",views.dairy,name="form"),
    path("<int:id>/update",views.update,name="update"),
    path("todo",views.todo,name="todo"),
    path("<int:id>/delete",views.delete,name="delete"),
    path("register",views.register,name="register"),
    path('login', views.login, name="login"),
    path('showtodo', views.show_todo, name="showtodo")
]