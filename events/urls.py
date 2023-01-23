from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('all/<str:pk>', views.events, name="all"),
    path('next/<str:pk>', views.nextEvents, name="next"),
    path('create', views.createEvent, name="create"),

    path('update/<str:pk>/<str:sk>', views.updateEvent, name="update"),
    path('delete/<str:pk>/<str:sk>', views.deleteEvent, name="delete"),
]


