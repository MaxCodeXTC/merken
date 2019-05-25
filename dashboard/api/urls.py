from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"configuration", views.ConfigViewSet)
router.register(r"message", views.HomeViewSet)
router.register(r"UsersAdmin", views.UserAdminViewSet)
# router.register(r"ProfileUsers", views.UserProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
