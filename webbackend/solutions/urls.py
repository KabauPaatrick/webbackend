from django.urls import path
from .views import SolutionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', SolutionViewSet, basename='solution')


urlpatterns = [
    path('show/', SolutionViewSet.as_view({'get': 'list'}), name='solution-list'),
    path('create/', SolutionViewSet.as_view({'post': 'create'}), name='solution-create'),
    path('<uuid:pk>/update/', SolutionViewSet.as_view({'put': 'update'}), name='solution-update'),
    path('<uuid:pk>/delete/', SolutionViewSet.as_view({'delete': 'destroy'}), name='solution-delete'),
]
