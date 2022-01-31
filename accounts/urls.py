from django.urls import path, include
from . import views

urlpatterns = [
    path("giris/", views.hesap_giris, name="login"),
    path("profil/", views.hesap_profil, name="profile"),
    path("cikis/", views.hesap_cikis, name="logout"),
]
