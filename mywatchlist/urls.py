# routings

from django.contrib import admin
from django.urls import path, include
from mywatchlist.views import show_watchlist, show_html, show_xml, show_json

app_name = 'mywatchlist'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_watchlist, name='show_watchlist'),
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]