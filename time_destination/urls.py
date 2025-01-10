from django.urls import path
from . import views

urlpatterns =[
    path('time_destination_insert/',views.time_destination_insert,name='time_destination_insert'),
    path('time_destination_list/',views.time_destination_list, name='time_destination_list'),
    path('edit_time_destination/<int:id>',views.edit_time_destination, name='edit_time_destination'),
    path('delete_time_destination/<int:id>',views.delete_time_destination, name='delete_time_destination'),
]