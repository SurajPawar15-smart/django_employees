from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import auth
from django.contrib.auth import login as auth_login

# Create your views here.
def register(request):
    if request.method == "POST":
       form=UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("register")
    
    form=UserCreationForm()
    context={
        'form':form  
    }
    return render(request,'accounts/register.html',context)


def login(request):
    if request.user.is_authenticated:
        print('The user is already logged in')
        return redirect('home')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to dashboard/home page

    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, "accounts/login.html", context)

def logout(request):
    auth.logout(request)
    return redirect('home')