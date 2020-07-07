"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import homepage_view,contact_view
from products.views import product_create_view,render_initail_data,dynamic_lookup_view,product_list_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage_view, name='home'),
    path('home/',homepage_view, name='home'),
    path('contact/',contact_view),
    #path('product/',product_detail_view),
    #path('create/',product_create_view)
    path('create/',render_initail_data),
    #path('products/<int:my_id>/',dynamic_lookup_view,name='products')
    path('products/',product_list_view,name='product-list'),
    #path('products/<str:>/',dynamic_lookup_view,) # cant usr another type
    path('products/<int:my_id>/',dynamic_lookup_view,name='product-detail')
    #path('products/<INT:ID>/delete',dynamic_delete_view,name='products')
]
