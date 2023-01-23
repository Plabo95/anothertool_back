from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('all/<str:pk>', views.clients, name="getAll"),
    path('create', views.createClient, name="create"),
    path('update/<str:pk>/<str:sk>', views.updateClient, name="update"),
    path('delete/<str:pk>/<str:sk>', views.deleteClient, name="delete"),
]


