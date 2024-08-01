# urls.py
from django.urls import path
from .views import PaymentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PaymentViewSet, basename='payment')

urlpatterns = [
    path('show/', PaymentViewSet.as_view({'get': 'list'}), name='payment-list'),
    path('create/', PaymentViewSet.as_view({'post': 'create'}), name='payment-create'),
    path('<uuid:pk>/update/', PaymentViewSet.as_view({'put': 'update'}), name='payment-update'),
    path('<uuid:pk>/delete/', PaymentViewSet.as_view({'delete': 'destroy'}), name='payment-delete'),
    path('<uuid:pk>/confirm/', PaymentViewSet.as_view({'post': 'confirm'}), name='payment-confirm'),
]
