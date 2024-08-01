from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_hologram, name='add_hologram'),
    path('edit/<int:id>/', views.edit_hologram, name='edit_hologram'),
    path('delete/<int:id>/', views.delete_hologram, name='delete_hologram'),
]
