from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from . models import Notification
from accounts.models import UserProfile

# Create your views here.
@login_required(login_url="/hesap/giris/")
def index(request):
    current_user = request.user
    getNotifications = Notification.objects.all().order_by("-notifDate")
    context = {
        "allnotif":getNotifications,
    }
    return render(request, "index.html", context)


@login_required(login_url="/hesap/giris/")
def dersler(request):
    return render(request, "dersler.html")


@login_required(login_url="/hesap/giris/")
def kullanicilar(request):
    allprofiles = UserProfile.objects.all()
    context = {
        'allprofiles':allprofiles,
    }
    return render(request, "kullanicilar.html", context)

@login_required(login_url="/hesap/giris/")
def error(request):
    return render(request, "error.html")