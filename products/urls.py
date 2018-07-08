from django.urls import path

from products.views import ProductView, ProductCreate, ProductList, ProductUpdate, ProductDelete

app_name = "products"
urlpatterns = [
    path("products/", ProductList.as_view(), name="list"),
    path("products/create/", ProductCreate.as_view(), name="create"),
    path("products/<pk>/edit/", ProductUpdate.as_view(), name="edit"),
    path("products/<pk>/delete/", ProductDelete.as_view(), name="delete"),
    path("products/<pk>/", ProductView.as_view(), name="view"),
    path("", ProductList.as_view(), name="list"),
]