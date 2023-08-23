from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import *
from .models import Profile
from market.models import Property
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
    profile = Profile.objects.get(id=request.user.id)
    custom_user = CustomUser.objects.get(id=request.user.id)

    listings = Property.objects.filter(owner=request.user)

    return render(request, "users/profile.html", {'profile': profile, 'c_user': custom_user, 'listings': listings})


@login_required
def EditProfileView(request):
    # user_instance = CustomUser.objects.get(id=request.user.id)
    profile_instance = Profile.objects.get(id=request.user.id)

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
    listings = Property.objects.filter(owner=request.user)
    return render(request, "users/my_listings.html", {'listings': listings})


@login_required
def AddPropertyView(request):

    if request.method == 'POST':
        form = AddPropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property_obj = form.save(commit=False)
            property_obj.owner = request.user
            property_obj.save()
            return redirect("users:my_listings")
    else:
        form = AddPropertyForm()
    return render(request, 'users/add_property_form.html', {'form': form})


def LogoutView(request):
    logout(request)
    return redirect("market:listing")


def DeleteView(request):
    request.user.delete()
    return redirect("users:login")
