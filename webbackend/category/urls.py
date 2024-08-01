from django.urls import path
from .views import CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CategoryViewSet, basename='product')

urlpatterns = [
    path('list/', CategoryViewSet.as_view({'get': 'list'}), name='product-list'),
    path('create/', CategoryViewSet.as_view({'post': 'create'}), name='product-create'),
    path('<uuid:pk>/update/', CategoryViewSet.as_view({'put': 'update'}), name='product-update'),
    path('<uuid:pk>/delete/', CategoryViewSet.as_view({'delete': 'destroy'}), name='product-delete'),
]

