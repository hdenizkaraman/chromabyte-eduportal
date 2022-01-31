from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import LoginForm 
from django.http import HttpResponse

# Create your views here.
def hesap_giris(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request, 'Disabled Account')
            else:
                messages.info(request, 'Kullanıcı Adı ya da Şifrenizi Tekrardan Kontrol Ediniz!')
    else:
        form = LoginForm()
    return render(request, 'giris.html', {'form':form})

def hesap_cikis(request):
    logout(request)
    return redirect('login')

def hesap_profil(request):
    current_user = request.user

    return render(request, 'profil.html')