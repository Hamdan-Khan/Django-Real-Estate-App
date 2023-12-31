from django.shortcuts import render, redirect
from .models import Property, PropertyType
from .forms import PropertyContactForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


# all listings view on the home page
def ListingsView(request):
    all_listings = Property.objects.all().order_by('-added_at')
    return render(request, 'market/home.html', {'listings': all_listings})


# listings view based on the type (house, shop, plot)
def TypesListingsView(request, property_type):
    # Get the PropertyType instance based on the property_type string
    property_type = property_type.capitalize()
    property_type_instance = get_object_or_404(
        PropertyType, name=property_type)

    # query the Property model using the retrieved instance
    listings = Property.objects.filter(type=property_type_instance)

    quantity = listings.count()

    if (quantity > 1):
        property_type = property_type+'s'

    return render(request, 'market/property_type_listing.html', {'listings': listings, 'type': property_type, 'quantity': quantity})


# listings detail view
def ListingDataView(request, listing_id):
    listing = Property.objects.get(id=listing_id)
    listing_title = listing.title[0:30] + "..."

    is_owner = False
    if (listing.owner == request.user):
        is_owner = True

    l_type = "Rent"
    if (listing.sale_type == 'Sell'):
        l_type = "Buy"

    return render(request, 'market/property_data.html', {'listing': listing, 'title': listing_title, 'type': l_type, 'isOwner': is_owner})


# contact user on the basis of listing
@login_required
def ListingContactView(request, listing_id):
    listing = Property.objects.get(id=listing_id)
    if (request.user == listing.owner):
        return render(request, 'market/404.html')
    listing_title = listing.title[0:30] + "..."

    l_type = "Rent"
    if (listing.sale_type == 'Sell'):
        l_type = "Buy"

    if request.method == "POST":
        form = PropertyContactForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = listing.owner
            message.property = listing
            message.save()
            return redirect("market:listing_data", listing_id)
    else:
        form = PropertyContactForm()

    context = {'title': listing_title, 'form': form,
               'type': l_type, 'listing': listing}
    return render(request, 'market/property_contact.html', context)


# listings view on the basis of sale_type: buy
def BuyView(request):
    listings = Property.objects.filter(sale_type="Sell").order_by("-added_at")
    quantity = listings.count()
    property_noun = "Property"
    if (quantity > 1):
        property_noun = "Properties"
    return render(request, 'market/buy.html', {'listings': listings, 'property_noun': property_noun, 'quantity': quantity})


# listings view on the basis of sale_type: rent
def RentView(request):
    listings = Property.objects.filter(sale_type="Rent").order_by("-added_at")
    quantity = listings.count()
    property_noun = "Property"
    if (quantity > 1):
        property_noun = "Properties"
    return render(request, 'market/rent.html', {'listings': listings, 'property_noun': property_noun, 'quantity': quantity})
