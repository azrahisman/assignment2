# routings

from django.contrib import admin
from django.urls import path, include
from mywatchlist.views import show_watchlist

app_name = 'mywatchlist'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_watchlist, name='show_watchlist'),
]