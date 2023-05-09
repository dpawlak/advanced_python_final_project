from django.urls import path

from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("index/", views.index, name="index"),
    path("transactions/", views.transactions, name="transactions"),
    path("customers/", views.customers, name="customers"),
    path("<str:item_name>/", views.detail, name="detail"),
]
