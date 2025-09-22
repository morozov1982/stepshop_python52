from django.urls import path

from mainapp.views import index, contacts, product, products, about

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('product/', product, name='product'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
]
