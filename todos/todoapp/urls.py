from django.urls import path
from . import views

urlpatterns = [
    path('', views.allTodos, name='allTodos'),
    path('delete_items/<int:pk>', views.delete_items, name='deleteitems'),
    path('updateitems/<int:pk>', views.update_items, name='updateitems'),
]