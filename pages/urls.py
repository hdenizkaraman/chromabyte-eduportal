from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dersler/', include("courses.urls")),
    path('kullanicilar/', views.kullanicilar, name="kullanicilar"),
    path('error/', views.error, name="error"),
]