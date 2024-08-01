# urls.py
from django.urls import path
from .views import ColorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ColorViewSet, basename='color')

urlpatterns = [
    path('show/', ColorViewSet.as_view({'get': 'list'}), name='color-list'),
    path('create/', ColorViewSet.as_view({'post': 'create'}), name='color-create'),
    path('<uuid:pk>/update/', ColorViewSet.as_view({'put': 'update'}), name='color-update'),
    path('<uuid:pk>/delete/', ColorViewSet.as_view({'delete': 'destroy'}), name='color-delete'),
]
