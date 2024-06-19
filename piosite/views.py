from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from piosite.forms import RegisterForm, ProfileForm
from piosite.models import Course, Favorite, Faculty, Speciality, Assignment, Profile


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('faculty_list')
    else:
        form = AuthenticationForm()
    return render(request, "html/logowanie.html", {"form": form})

def home_view(request):
    return HttpResponse("<h1>hello world</h1>")