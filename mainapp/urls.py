from django.urls import path

from mainapp.views import index, contacts, product

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('product/', product, name='product'),
    path('contacts/', contacts, name='contacts'),
]
