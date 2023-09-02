from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.RegisterView, name="register"),
    path("login/", views.LoginView, name="login"),
    path("profile/", views.ProfileView, name="profile"),
    path("profile/edit", views.EditProfileView, name="edit_profile"),
    path("my_listings/", views.MyListingsView, name="my_listings"),
    path("my_listings/add", views.AddPropertyView, name="add_listing"),
    path("my_listings/edit/<int:listing_id>",
         views.EditPropertyView, name="edit_listing"),
    path("my_listings/delete/<int:listing_id>",
         views.DeleteListingView, name="delete_listing"),
    path("<int:profile_id>/profile", views.OtherProfileView, name="other_profile"),
    path("<int:profile_id>/profile/contact",
         views.ContactProfileView, name="contact_profile"),
    path("<int:profile_id>/profile/listings",
         views.OtherListingsView, name="other_profile_listings"),
    path("logout/", views.LogoutView, name="logout"),
    path("delete_account/confirmation",
         views.DeleteConfirmationView, name="delete_confirmation"),
    path("delete_account/", views.DeleteView, name="delete_account"),
]
