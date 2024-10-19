from django.contrib import admin
from django.urls import path, include
from .views import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Redirect to login first
    path('signup/', include('LibManager.urls')),  # Include signup from LibManager app
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Logout view
    path('home/', home, name='home'),  # Home page URL
    path('books/', include('LibManager.urls')),  # Include book-related URLs
]
