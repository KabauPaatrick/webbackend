from django.urls import path
from .views import LicenseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', LicenseViewSet, basename='license')


urlpatterns = [
    path('show/', LicenseViewSet.as_view({'get': 'list'}), name='license-list'),
    path('create/', LicenseViewSet.as_view({'post': 'create'}), name='license-create'),
    path('<uuid:pk>/update/', LicenseViewSet.as_view({'put': 'update'}), name='license-update'),
    path('<uuid:pk>/delete/', LicenseViewSet.as_view({'delete': 'destroy'}), name='license-delete'),
]