# appropriate urls urls to map our views

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet

router = DefaultRouter()
router.register(r"countries", TaskViewSet)

urlpatterns = [
    path("", include(router.urls))
]