# TODO: Implement Routings Here

from django.contrib import admin
from django.urls import path, include
from katalog.views import show_catalog

app_name = 'katalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_catalog, name='show_catalog'),
]