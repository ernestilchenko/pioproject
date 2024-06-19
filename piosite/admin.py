from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from .models import Course, Favorite, Faculty, Speciality, Assignment, Profile


class CustomAdminSite(AdminSite):
    site_header = "Admin Panel"
    site_title = "Admin Panel"
    index_title = "Welcome to Admin Panel"


admin_site = CustomAdminSite(name='custom_admin')


class FavoriteInline(admin.TabularInline):
    model = Favorite
    extra = 0


class UserAdmin(BaseUserAdmin):
    inlines = (FavoriteInline,)
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('id', 'username', 'first_name', 'last_name', 'email')
    ordering = ('id',)


# Register the User model with the custom admin site
admin_site.register(User, UserAdmin)


class CourseAdmin(admin.ModelAdmin):
    inlines = (FavoriteInline,)
    list_display = ('course_id', 'title', 'image', 'video_file', 'zip_files')
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


admin_site.register(Course, CourseAdmin)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
    list_filter = ('user', 'course')


admin_site.register(Favorite, FavoriteAdmin)


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin_site.register(Faculty, FacultyAdmin)


class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin_site.register(Speciality, SpecialityAdmin)


class AssignmentAdmin(admin.ModelAdmin):
    model = Assignment
    list_display = ['user', 'course', 'assignment_decription', 'assignment_progress', 'assignment_deadline']


admin_site.register(Assignment, AssignmentAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'preview')

    def preview(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" style="max-height: 200px;">')
        return ""

    preview.short_description = 'Avatar Preview'


admin_site.register(Profile, ProfileAdmin)
