# locations/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, DropOffPointViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet, basename='location')
router.register(r'dropoff-points', DropOffPointViewSet, basename='dropoff-point')

urlpatterns = [
    path('locations/list/', LocationViewSet.as_view({'get': 'list'}), name='location-list'),
    path('locations/create/', LocationViewSet.as_view({'post': 'create'}), name='location-create'),
    path('locations/<uuid:pk>/update/', LocationViewSet.as_view({'put': 'update'}), name='location-update'),
    path('locations/<uuid:pk>/delete/', LocationViewSet.as_view({'delete': 'destroy'}), name='location-delete'),
    
    path('dropoff-points/list/', DropOffPointViewSet.as_view({'get': 'list'}), name='dropoff-point-list'),
    path('dropoff-points/create/', DropOffPointViewSet.as_view({'post': 'create'}), name='dropoff-point-create'),
    path('dropoff-points/<uuid:pk>/update/', DropOffPointViewSet.as_view({'put': 'update'}), name='dropoff-point-update'),
    path('dropoff-points/<uuid:pk>/delete/', DropOffPointViewSet.as_view({'delete': 'destroy'}), name='dropoff-point-delete'),
]

urlpatterns += router.urls
