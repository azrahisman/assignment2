from django.shortcuts import render
from mywatchlist.models import WatchlistItem

# views
def show_watchlist(request):
    data_watchlist_item = WatchlistItem.objects.all()
    context = {
        'list_item': data_watchlist_item,
        'name': 'Azra'
    }
    return render(request, "mywatchlist.html", context)