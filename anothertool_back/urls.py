from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from user.views import MyTokenObtainPairView

router = DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/token', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/user/refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', include('user.urls')),

    path('api/', include('clients.urls')),
    path('api/', include('orders.urls')),
    path("api/", include("cars.urls")),
    path('api/', include('invoices.urls')),
    path("api/", include("workshop.urls")),
]
