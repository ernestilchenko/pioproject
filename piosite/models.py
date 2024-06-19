from django.contrib.auth.models import User, AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    course_id = models.AutoField(primary_key=True, verbose_name='Course ID')
    title = models.CharField(max_length=200, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='images/', verbose_name='Image', null=True, blank=True)
    video_file = models.FileField(
        upload_to='videos/',
        verbose_name='Video File',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi', 'mkv'])],
        null=True,
        blank=True
    )
    zip_files = models.FileField(
        upload_to='zip_files/',
        verbose_name='Zip Files',
        validators=[FileExtensionValidator(allowed_extensions=['zip'])],
        null=True,
        blank=True
    )
    is_favorite = models.BooleanField(default=True)  # Добавляем поле для проверки нахождения курса в избранных

    @property
    def is_favorite(self):
        request = getattr(self, '_request', None)
        if request and request.user.is_authenticated:
            return Favorite.objects.filter(user=request.user, course=self).exists()
        return False

    def set_request(self, request):
        self._request = request


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'course')


class Faculty(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')

    def __str__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')

    def __str__(self):
        return self.name


class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignment')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments', verbose_name='Course')
    assignment_decription = models.TextField(verbose_name='Description')
    assignment_progress = models.DecimalField(max_digits=3, decimal_places=0, default=0, verbose_name='Progress')
    assignment_deadline = models.DateTimeField(verbose_name='Deadline', null=True, blank=True)
