from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeroPageViewSet

router = DefaultRouter()
router.register(r'heropage', HeroPageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
