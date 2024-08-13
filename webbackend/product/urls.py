from django.urls import path
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ProductViewSet, basename='product')

urlpatterns = [
    path('list/', ProductViewSet.as_view({'get': 'list'}), name='product-list'),
    path('create/', ProductViewSet.as_view({'post': 'create'}), name='product-create'),
    path('<uuid:pk>/update/', ProductViewSet.as_view({'put': 'update'}), name='product-update'),
    path('<uuid:pk>/delete/', ProductViewSet.as_view({'delete': 'destroy'}), name='product-delete'),
]

urlpatterns += router.urls
