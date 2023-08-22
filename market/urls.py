from django.urls import path
from .views import *

app_name = "market"

urlpatterns = [
    path('', ListingsView, name="listing"),
    path('buy/<str:property_type>', TypesListingsView,
         name="property_type_listing"),
    path('property/<int:listing_id>', ListingDataView, name="listing_data"),
    path('buy/', BuyView, name="buy"),
    path('rent/', RentView, name="rent"),
]
