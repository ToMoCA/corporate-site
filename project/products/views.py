from django.views import generic

from .models import Product

class IndexView(generic.ListView):
    template_name = 'products/index.html'
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
