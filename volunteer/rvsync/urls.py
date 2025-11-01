from django.urls import path
from . import views

urlpatterns = [
    path('api/events/', views.events_api, name='events_api'),
    path('', views.calendar_view, name='calendar_view'),
    path('api/add_event/', views.add_event_api, name='add_event_api'),
    path('api/delete_event/<int:pk>/', views.delete_event_api, name='delete_event_api'),

]
