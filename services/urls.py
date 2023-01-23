from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('services/<str:pk>', views.services, name="services"),
    path('createservice', views.createService, name="createService"),
    path('updateservice/<str:pk>/<str:sk>', views.updateService, name="updateService"),
    path('deleteservice/<str:pk>/<str:sk>', views.deleteService, name="deleteService"),    
]


