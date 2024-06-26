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

@login_required
def harmonogram(request):
    return render(request, 'html/harmonogram.html')

@login_required
def course(request):
    return render(request, 'html/course.html')

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    return render(request, 'html/course.html', {'course': course})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, "html/rejestracja.html", {"form": form})
def course_list(request):
    courses = Course.objects.all()
    user = request.user
    for course in courses:
        course.set_request(request)
    return render(request, 'html/favorites_list.html', {'courses': courses, 'user': user})

@login_required
def add_to_favorites(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    _, created = Favorite.objects.get_or_create(user=request.user, course_id=course_id, course=course, )
    if created:
        messages.success(request, 'Course added to favorites successfully!')
    else:
        messages.info(request, 'Course is already in your favorites.')
    return redirect('favorites_list')

@login_required
def delete_course(request, course_id):
    favorite = get_object_or_404(Favorite, user=request.user, course_id=course_id)
    favorite.delete()
    return redirect('faculty_list')

@login_required
def user_profile(request):
    user = request.user
    return render(request, 'html/index.html', {'user': user})

def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def select_faculty_and_speciality_and_favorites_list(request):
    faculties = Faculty.objects.all()
    user = request.user
    specialities = Speciality.objects.all()
    favorites = Favorite.objects.filter(user=request.user).select_related('course')

    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'html/course_list.html', {
        'faculties': faculties,
        'favorites': favorites,
        'specialities': specialities,
        'user': user,
        'form': form,
        'profile': profile,
    })

def custom_404_view(request, exception):
    return redirect('faculty_list')

@csrf_exempt
def add_to_favorites(request, course_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            favorite, created = Favorite.objects.get_or_create(user=request.user, course_id=course_id)
            if created:
                return JsonResponse({'message': 'Course added to favorites successfully!'}, status=201)
            else:
                return JsonResponse({'message': 'Course is already in favorites!'}, status=400)
        else:
            return JsonResponse({'message': 'User is not authenticated!'}, status=401)
    else:
        return JsonResponse({'message': 'Invalid request method!'}, status=405)

@login_required
def harmonogram(request):
    assignments = Assignment.objects.all()
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'html/harmonogram.html', {'user': user, 'assignments': assignments, 'profile': profile})