from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dersler, name="dersler"),
    path('<slug:listslug>/<int:videoindex>/', views.egitimvideo, name="egitimvideo"),
    path('dersal/<slug:listslug>/', views.dersal, name="dersal"),
    path('videobitir/<slug:videoslug>', views.videobitir, name="videobitir"),
]