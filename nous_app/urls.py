from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.items_list, name='items_list'),
    path('', views.items_add, name='items_add'),
    path('<int:id>/', views.items_add, name='items_edit'),
    path('delete/<int:id>/', views.items_delete, name='items_delete'),
]