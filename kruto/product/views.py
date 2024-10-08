from django.shortcuts import render, redirect
from .models import Material, Category
from django.views.generic import DetailView
from .models import PriceList, Companies


def materials_list(request):
    category = request.GET.get('category')
    categories = Category.objects.all()
    price_lists = PriceList.objects.all()
    if category:
        materials = Material.objects.filter(category=category)
    else:
        materials = Material.objects.all()
    return render(request, 'product/product_main.html', {'materials': materials, 'current_category': category, 'categories': categories, 'price_lists': price_lists })


def home(request):
    materials = Material.objects.all()
    price_lists = PriceList.objects.all()
    companies = Companies.objects.all()
    
    return render(request, 'home/home.html', {'materials': materials, "price_lists": price_lists, 'companies': companies})


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'detail/detail.html'
    context_object_name = 'materials'
    
    
def about(request):
    materials = Material.objects.all()
    companies = Companies.objects.all()
    return render(request, 'about/about.html', {'materials': materials, 'companies': companies})
    

from .forms import CallbackForm

def callback_view(request):
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CallbackForm()

    return render(request, 'callback_form.html', {'form': form})


def index(request):
    price_lists = PriceList.objects.all()  # Извлекаем все прайс-листы
    return render(request, 'your_template.html', {'price_lists': price_lists})


def contacts(request):
    return render(request, "contacts/contacs.html", {})
