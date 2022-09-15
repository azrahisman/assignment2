from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        'list_item': data_catalog_item,
        'name': 'Azra'
    }
    return render(request, "katalog.html", context)