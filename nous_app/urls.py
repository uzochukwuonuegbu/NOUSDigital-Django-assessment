from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.items_list),
    path('', views.items_add),
    # path('', views.items_delete),
]