from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"users/user.html")
def login_view(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"users/login.html",{
                "message":"Invalid credentials."
            })    
    return render(request,"users/login.html")

def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{
        "message":"Logged Out."
    })

def register_view(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj=form.save()
        return HttpResponseRedirect(reverse('login'))
    return render(request,"users/register.html",{
        "form":form
    })