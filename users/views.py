from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import *
from market.models import Property, PropertyImage
from django.contrib.auth.decorators import login_required


def RegisterView(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
    else:
        form = RegistrationForm()
    return render(request, "users/register.html", {"form": form})


def LoginView(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("market:listing")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


# own profile view
@login_required
def ProfileView(request):
    custom_user = request.user
    profile = custom_user.profile

    listings = Property.objects.filter(owner=custom_user).order_by("-added_at")

    listings = listings[:3]

    context = {'profile': profile, 'c_user': custom_user,
               'listings': listings, 'is_owner': True}
    return render(request, "users/profile.html", context)


@login_required
def EditProfileView(request):
    profile_instance = request.user.profile

    if request.method == 'POST':
        profile_form = ProfileChangeForm(
            request.POST, request.FILES, instance=profile_instance)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("users:profile")
    else:
        profile_form = ProfileChangeForm(instance=profile_instance)

    return render(request, "users/edit_profile.html", {'form': profile_form, })


@login_required
def MyListingsView(request):
    listings = Property.objects.filter(
        owner=request.user).order_by("-added_at")
    return render(request, "users/my_listings.html", {'listings': listings, 'my_listings': True})


def OtherListingsView(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    owner = profile.user
    listings = Property.objects.filter(
        owner=owner).order_by("-added_at")
    return render(request, "users/my_listings.html", {'listings': listings, 'profile': profile})


@login_required
def AddPropertyView(request):

    if request.method == 'POST':
        images = request.FILES.getlist('images')
        form = AddPropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property_obj = form.save(commit=False)
            property_obj.owner = request.user
            property_obj.save()
            for image in images:
                PropertyImage.objects.create(
                    property=property_obj,
                    file=image
                )
            return redirect("users:my_listings")
    else:
        form = AddPropertyForm()
    return render(request, 'users/add_property_form.html', {'form': form})


@login_required
def EditPropertyView(request, listing_id):
    property_instance = Property.objects.get(id=listing_id)
    if request.method == 'POST':
        form = AddPropertyForm(request.POST, request.FILES,
                               instance=property_instance)
        if form.is_valid():
            form.save()
            return redirect("market:listing_data", listing_id)
    else:
        form = AddPropertyForm(instance=property_instance)
        print(form)
    return render(request, 'users/add_property_form.html', {'form': form, 'edit_mode': True})


@login_required
def DeleteListingView(request, listing_id):
    # retrieves the listing to delete
    listing = get_object_or_404(Property, id=listing_id)
    listing.delete()
    return redirect("users:my_listings")


# other users profile view
def OtherProfileView(request, profile_id):
    # checks if user is logged in and if request is of the user that is logged in, he will be redirected to his own profile
    if request.user.id != None:
        if request.user.profile.id == profile_id:
            return redirect("users:profile")
    else:
        profile = Profile.objects.get(id=profile_id)
        custom_user = profile.user

        listings = Property.objects.filter(
            owner=custom_user).order_by("-added_at")

        listings = listings[:3]

        return render(request, "users/profile.html", {'profile': profile, 'c_user': custom_user, 'listings': listings})


# contact through profile
def ContactProfileView(request, profile_id):
    receiver_profile = Profile.objects.get(id=profile_id)
    listings = Property.objects.filter(owner=receiver_profile.user)

    if request.method == "POST":
        data = request.POST
        form = ProfileContactForm(data)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = receiver_profile.user
            selected_listing = data['selected_listing']
            if selected_listing != 'none':
                message.property = listings.get(id=selected_listing)
            message.save()
            return redirect("users:other_profile", profile_id)
    else:
        form = ProfileContactForm()
    context = {'profile': receiver_profile, 'form': form, 'listings': listings}
    return render(request, 'users/contact_profile.html', context)


def LogoutView(request):
    logout(request)
    return redirect("market:listing")


@login_required
def DeleteConfirmationView(request):
    return render(request, "users/delete_profile_confirmation.html")


@login_required
def DeleteView(request):
    request.user.delete()
    return redirect("market:listing")
