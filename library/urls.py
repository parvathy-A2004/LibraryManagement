from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('add-book/', views.add_book, name='add_book'),
    path('edit-book/<int:id>/', views.edit_book, name='edit_book'),
    path('delete-book/<int:id>/', views.delete_book, name='delete_book'),

    path('students/', views.student_list, name='student_list'),
    path('add-student/', views.add_student, name='add_student'),
    path('edit-student/<int:id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),

    path('issues/', views.issue_list, name='issue_list'),
    path('issue-book/', views.issue_book, name='issue_book'),

    path('return-book/<int:id>/', views.return_book, name='return_book'),
]