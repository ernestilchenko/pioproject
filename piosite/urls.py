from django.urls import path

from . import views
from .admin import admin_site
from .views import *

handler404 = 'pio_site.views.custom_404_view'
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('favorites/add/<int:course_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorites/', views.course_list, name='favorites_list'),
    path('favorites/add/<int:course_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('', views.home_view, name='home'),
    path('courses/delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('logout/', views.logout, name='logout'),
    path('courses/', views.select_faculty_and_speciality_and_favorites_list, name='faculty_list'),
    path('harmonogram/', views.harmonogram, name='harmonogram'),
    path('course/', views.course, name='course'),
    path('harmonogram/', views.harmonogram, name='harmonogram'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('admin/', admin_site.urls, name='admin_site')
]
