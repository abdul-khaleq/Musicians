from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_musician, name='add_musician'),
    path('delete/<int:id>', views.delete_album, name='delete_album'),
    path('edit/<int:id>', views.edit_musician, name='edit_musician'),
]