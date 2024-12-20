
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', include('main.urls')),  # Include app1 URLs
    path('/', include('module.urls')),  # For authentication
]