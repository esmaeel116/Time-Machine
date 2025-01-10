from django.urls import path
from . import views

urlpatterns =[
    path('time_traveler_insert/', views.time_traveler_insert, name='time_traveler_insert'),
    path('time_traveler_list/', views.time_traveler_list, name='time_traveler_list'),
    path('edit_time_traveler/<int:id>', views.edit_time_traveler, name='edit_time_traveler'),
    path('delete_time_traveler/<int:id>', views.delete_time_traveler, name='delete_time_traveler'),
    path('detail_time_traveler/<int:id>', views.detail_time_traveler, name='detail_time_traveler'),
]