from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='main_user_set',  # This ensures no conflict with the default 'user_set'
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='main_user_permissions',  # This ensures no conflict with the default 'user_permissions'
        blank=True
    )
    
    def is_student(self):
        return self.role == 'student'

    def is_teacher(self):
        return self.role == 'teacher'
    
    
class Notes(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='notes/')
    uploaded_by = models.ForeignKey('User', on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)