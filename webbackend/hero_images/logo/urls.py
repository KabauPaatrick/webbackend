from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LogoViewSet

router = DefaultRouter()
router.register(r'users', LogoViewSet, basename='user-registration')

urlpatterns = [
    path('show/', LogoViewSet.as_view({'get': 'list'}), name='user-list'),
    path('create/', LogoViewSet.as_view({'post': 'create'}), name='user-create'),
    path('<uuid:pk>/update/', LogoViewSet.as_view({'put': 'update'}), name='user-update'),
    path('<uuid:pk>/delete/', LogoViewSet.as_view({'delete': 'destroy'}), name='user-delete'),
]

urlpatterns += router.urls
