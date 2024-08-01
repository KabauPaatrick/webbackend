from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet

router = DefaultRouter()
router.register('', TicketViewSet, basename='ticket')

urlpatterns = [
    path('show/',TicketViewSet.as_view({'get':'list'}), name='ticket-show'),
    path('create/', TicketViewSet.as_view({'post': 'create'}), name='ticket-create'),
    path('<uuid:pk>/update/', TicketViewSet.as_view({'put': 'update'}), name='ticket-update'),
    path('<uuid:pk>/delete/', TicketViewSet.as_view({'delete': 'destroy'}), name='ticket-delete'),
] + router.urls
