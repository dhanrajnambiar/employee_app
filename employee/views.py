from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from .forms import LoginForm
# Create your views here.

def user_login(request):
    if request.method == "POST":
        l_form = LoginForm(request.POST)
        if l_form.is_valid():
            user_name, password = l_form.cleaned_data.get('User_Name'), l_form.cleaned_data.get('Password')
            u = authenticate(user_name, password)
            if not u:
                login(request, u)
                print(u)

    if request.method == "GET":
        l_form = LoginForm
        return render(request, 'login.html', {'form': l_form})

# @login_required
def home_page(request):
    return render(request, 'user_home.html')
