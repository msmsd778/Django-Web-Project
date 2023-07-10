from django.urls import path

from . import views


app_name = "main"

urlpatterns = [
    path('', views.index_view, name="index"),
    path('about-us/', views.about_view, name="about"),
    path('contact-us/', views.contact_view, name="contact"),
    path('contracts/', views.contract_view, name="contract"),
    path('gallery/', views.gallery_view, name="gallery"),
    path('products/<str:slug>/', views.category_view, name="category"),
    path('products/<str:slug1>/<str:slug2>/', views.product_view, name="product"),
]
