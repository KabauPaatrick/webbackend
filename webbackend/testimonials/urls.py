from django.urls import path
from .views import TestimonialViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TestimonialViewSet, basename='testimonial')

urlpatterns = [
    path('show/', TestimonialViewSet.as_view({'get': 'list'}),name='testimonial-list'),
    path('create/',TestimonialViewSet.as_view({'post': 'create'}), name='testimonial-list-create'),
    path('<int:id>/update/', TestimonialViewSet.as_view({'put':'update'}), name='testimonial-update'),
    path('<int:id>/delete/', TestimonialViewSet.as_view({'delete': 'destroy'}), name='testimonial-delete'),
]
