from django.urls import path
from django.urls import path
from . import views

app_name = 'shop' 
urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('<slug:cat_slug>/', views.product_list, name='product-list-by-cat'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product-detail'),
]