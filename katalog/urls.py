# TODO: Implement Routings Here

from django.contrib import admin
from django.urls import path, include
from katalog.views import show_catalog
from katalog.views import register
from katalog.views import login_user
from katalog.views import logout_user

app_name = 'katalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_catalog, name='show_catalog'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]