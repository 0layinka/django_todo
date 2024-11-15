from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('create/', views.create, name = 'create'),
    path('read/<int:pk>', views.read, name = 'read'),
    path('update/<int:pk>', views.update, name = 'update'),
    path('delete/<int:pk>', views.delete, name = 'delete'),
]