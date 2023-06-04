from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('bitcoin_prices', views.bitcoin_prices),
]
