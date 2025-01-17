from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addBook, name='addBook'),
    path('view/', views.viewBookList, name='viewBookList'),
    path('view/<int:book_id>/', views.bookView, name='bookView'),
    path('search/', views.searchBook, name='searchBook'),
    path('delete/', views.deleteBook, name='deleteBook'),
    path('signup/', views.signup, name='signup'),  # Signup view
    path('login/', views.login_view, name='login'),  # Login view
]
