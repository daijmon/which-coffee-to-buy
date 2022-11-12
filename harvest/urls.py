from django.urls import path

from .views import CoffeeFromCountryView

urlpatterns = [path("", CoffeeFromCountryView.as_view(), name="coffee-from-country")]
