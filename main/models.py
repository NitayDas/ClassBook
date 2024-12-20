from django.contrib.auth.models import AbstractUser
from django.db import models

# Define the Preference model for multiple choices (for students)
class Preference(models.Model):
    name = models.CharField(max_length=100, choices=[
        ('mathematics', 'Mathematics'),
        ('science', 'Science'),
        ('computer_science', 'Computer Science & Technology'),
        ('engineering', 'Engineering'),
        ('social_studies', 'Social Studies'),
        ('languages', 'Languages'),
        ('arts', 'Arts'),
        ('physical_education', 'Physical Education'),
        ('environmental_studies', 'Environmental Studies'),
        ('health_and_wellness', 'Health and Wellness'),
        ('economics', 'Economics'),
        ('business_and_management', 'Business and Management'),
        ('philosophy', 'Philosophy'),
        ('psychology', 'Psychology'),
        ('literature', 'Literature'),
        ('music', 'Music'),
        ('religious_studies', 'Religious Studies'),
        ('political_science', 'Political Science'),
        ('vocational_training', 'Vocational Training'),
        ('media_communication_studies', 'Media and Communication Studies'),
    ])

    def __str__(self):
        return self.name
    
class StudyGroup(models.Model):
    name = models.CharField(max_length=20, choices=[
        ('science', 'Science'),
        ('arts', 'Arts'),
        ('commerce', 'Commerce'),
    ])

    def __str__(self):
        return self.name


# Custom User model that extends AbstractUser
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    
    GROUP_CHOICE = [
        ('science', 'Science'),
        ('arts', 'Arts'),
        ('commerce', 'Commerce'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    # studygroup = models.CharField(max_length=10, choices=GROUP_CHOICE, default='science')
    # groups = models.ManyToManyField(StudyGroup, blank=True)
    # preferences = models.ManyToManyField(Preference, blank=True)
    preferences = models.TextField(max_length=2000, blank=True, null =True)
    groups = models.CharField(max_length=20,choices=GROUP_CHOICE, default='science', blank=True, null =True)

    def __str__(self):
        return self.username
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

# Notes model
class Notes(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='notes/')
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
