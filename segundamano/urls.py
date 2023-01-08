"""segundamano URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from products import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('products', product_views.list, name='products'),
    path('products/fav', product_views.fav, name='fav_products'),
    path('products/new', product_views.new, name='new_product'),
    path('product/details/<str:id>', product_views.details, name='details_product'),
    path('product/like/<str:id>', product_views.like, name='like_product'),
    path('product/unlike/<str:id>', product_views.unlike, name='unlike_product'),
    path('product/delete/<str:id>', product_views.delete, name='delete_product'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
