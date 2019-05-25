from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"configuration", views.ConfigViewSet)
router.register(r"message", views.HomeViewSet)
router.register(r"users", views.UserListView)
router.register(r"users", views.UserDetailView)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
