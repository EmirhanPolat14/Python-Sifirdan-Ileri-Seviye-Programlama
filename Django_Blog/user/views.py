from django.shortcuts import render,HttpResponse,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,authenticate
from django.contrib.auth import logout as auth_logout

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)
           
        newUser.save()
        auth_login(request,newUser)
        messages.success(request,"Başarı ile kayıt olundu")
           
        return redirect("index")
       
    context = {
        "form" : form
        }
    return render(request,"register.html",context)


@csrf_exempt
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context) 
        
        messages.success(request,"Başarı ile giriş yaptınız...")
        auth_login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logout(request):
    auth_logout(request)
    messages.success(request,"Hesaptan Çıkış Yapıldı.")
    return redirect("index")
