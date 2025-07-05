from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),  # includes your app’s URLs
]

# Serving media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from notes import views  # <-- add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # <-- add this
    path('upload/', views.upload_notes, name='upload'),
    path('browse/', views.browse_notes, name='browse'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
