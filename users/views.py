from django.shortcuts import render, redirect
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


@login_required
def ProfileView(request):
    custom_user = request.user
    profile = custom_user.profile

    listings = Property.objects.filter(owner=custom_user).order_by("-added_at")

    listings = listings[:3]

    return render(request, "users/profile.html", {'profile': profile, 'c_user': custom_user, 'listings': listings})


@login_required
def EditProfileView(request):
    # user_instance = CustomUser.objects.get(id=request.user.id)
    profile_instance = request.user.profile

    if request.method == 'POST':
        profile_form = ProfileChangeForm(
            request.POST, request.FILES, instance=profile_instance)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("users:profile")
    else:
        profile_form = ProfileChangeForm(instance=profile_instance)

    return render(request, "users/edit_profile.html", {'form2': profile_form, })


@login_required
def MyListingsView(request):
    listings = Property.objects.filter(
        owner=request.user).order_by("-added_at")
    for listing in listings:
        all_images = listing.property_pics.all()
        if all_images:
            print([x.file.url for x in all_images])
    return render(request, "users/my_listings.html", {'listings': listings})


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
    return render(request, 'users/add_property_form.html', {'form': form, 'edit_mode': True})


def LogoutView(request):
    logout(request)
    return redirect("market:listing")


def DeleteView(request):
    request.user.delete()
    return redirect("market:listing")
