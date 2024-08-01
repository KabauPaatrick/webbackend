from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationViewSet

router = DefaultRouter()
router.register(r'users', UserRegistrationViewSet, basename='user-registration')

urlpatterns = [
    path('show/', UserRegistrationViewSet.as_view({'get': 'list'}), name='user-list'),
    path('create/', UserRegistrationViewSet.as_view({'post': 'create'}), name='user-create'),
    path('<uuid:pk>/update/', UserRegistrationViewSet.as_view({'put': 'update'}), name='user-update'),
    path('<uuid:pk>/delete/', UserRegistrationViewSet.as_view({'delete': 'destroy'}), name='user-delete'),
]

urlpatterns += router.urls
