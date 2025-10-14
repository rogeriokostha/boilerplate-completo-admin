from django.urls import path
from .views import CountryListView, StateListView, CityListView, AddressCreateView

urlpatterns = [
    path("countries/", CountryListView.as_view(), name="country_list"),
    path("states/", StateListView.as_view(), name="state_list"),
    path("cities/", CityListView.as_view(), name="city_list"),
    path("addresses/", AddressCreateView.as_view(), name="address_create"),
]
