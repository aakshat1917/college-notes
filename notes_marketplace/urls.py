# notes_marketplace/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),  # ✅ this includes your app's URLs for homepage and others
]
