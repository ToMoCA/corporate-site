from django.views import generic
from django.shortcuts import render, redirect

from .models import Product

def home_page(request):
    return render(request, 'products/index.html')


def contact(request):
    from .forms import ContactForm
    from django.core.mail import EmailMessage
    from django.template import Context
    from django.template.loader import render_to_string

    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            company = request.POST.get(
                'company'
                , '')
            division = request.POST.get(
                'division'
                , '')
            name = request.POST.get(
                'name'
                , '')
            address = request.POST.get(
                'address'
                , '')
            phone_number = request.POST.get(
                'phone_number'
                , '')
            email = request.POST.get(
                'email'
                , '')
            content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            context = {
                'company'      : company,
                'division'     : division,
                'name'         : name,
                'address'      : address,
                'phone_number' : phone_number,
                'email'        : email,
                'content'      : content,
            }
            content = render_to_string('products/contact_template.txt', context)

            email = EmailMessage(
                subject = "[ToMoCA] Thank you for contacting us",
                body = content,
                to = ["ks6088ts@gmail.com", "take@tomoca.jp", email],
            )
            email.send()
            return redirect('/')
        else:
            error_message = '入力データが不正です。再度入力をお願いします。/ Input data is invalid. Please fill in correct data.'
            return render(request, 'products/contact.html', {
                'error': error_message,
                'form': form_class,
            })

    return render(request, 'products/contact.html', {
        'form': form_class,
    })


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
