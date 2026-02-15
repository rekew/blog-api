from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.views import RegisterViewSet


# Users router
users_router = DefaultRouter()
users_router.register("auth/register", RegisterViewSet, basename="register")


urlpatterns = [
    path("admin/", admin.site.urls),

    # Users
    path("api/", include(users_router.urls)),

    # Blogs
    path("api/", include("apps.blogs.urls")),

    # JWT
    path("api/auth/token/", TokenObtainPairView.as_view(),
         name="token_obtain_pair"),
    path("api/auth/token/refresh/",
         TokenRefreshView.as_view(), name="token_refresh"),
]
