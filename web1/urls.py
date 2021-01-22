from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("<int:id>/customers",views.customers,name="customers"),
    path("products",views.products,name="products"),
    path("orderform",views.create_order, name='createorder'),
    path("customerform",views.create_customer, name='createcustomer'),
    path("updateorder/<str:id>",views.update_order, name='updateorder'),
    path("deleteorder/<str:id>",views.deleteorder,name="deleteorder"),
    path("updatecustomer/<str:id>",views.update_customer,name="updatecustomer"),
    path("deletecustomer/<str:id>",views.deletecustomer,name="deletecustomer"),
    path("register",views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logoutuser,name='logout'),
    path("userpage",views.userpage,name="userpage"),
    path("account",views.account,name="account")
]
