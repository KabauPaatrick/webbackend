# urls.py
from django.urls import path
from .views import BrandViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', BrandViewSet, basename='brand')

urlpatterns = [
    path('show/', BrandViewSet.as_view({'get': 'list'}), name='brand-list'),
    path('create/', BrandViewSet.as_view({'post': 'create'}), name='brand-create'),
    path('<uuid:pk>/update/', BrandViewSet.as_view({'put': 'update'}), name='brand-update'),
    path('<uuid:pk>/delete/', BrandViewSet.as_view({'delete': 'destroy'}), name='brand-delete'),
]
