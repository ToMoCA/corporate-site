from django.views import generic
from django.shortcuts import render

from .models import Product

def home_page(request):
    return render(request, 'products/index.html')

class IndexView(generic.ListView):
    template_name = 'products/list.html'
    context_object_name = 'product_list'
    # paginate_by = 5
    ordering = '-pk'

    def get_queryset(self):
        return Product.objects.all()

class DetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'

    def get_queryset(self):
        return Product.objects.all()
