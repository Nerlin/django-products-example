from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from products.forms import ProductForm, ProductFilter
from products.models import Product


class ProductCreate(PermissionRequiredMixin, CreateView):
    template_name = "products/form.html"
    model = Product
    form_class = ProductForm
    permission_required = "products.add_product"
    raise_exception = True


class ProductUpdate(PermissionRequiredMixin, UpdateView):
    template_name = "products/form.html"
    model = Product
    form_class = ProductForm
    permission_required = "products.change_product"


class ProductDelete(DeleteView):
    template_name = "products/delete.html"
    model = Product
    success_url = reverse_lazy("products:list")
    permission_required = "products.delete_product"


class ProductView(DetailView):
    template_name = "products/view.html"
    model = Product


class ProductList(FilterView):
    template_name = "products/list.html"
    paginate_by = 10
    filterset_class = ProductFilter
    queryset = Product.objects.order_by("id")
