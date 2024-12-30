from django.urls import path
from library_app import views

urlpatterns = [
    path('library_home/', views.library_home, name='library_home'),
    path('add_book/', views.add_book, name='add_book'),
    path('update_book/<int:book_id>/', views.update_book, name='update_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
