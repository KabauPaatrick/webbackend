# urls.py
from django.urls import path
from .views import EnquiryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', EnquiryViewSet, basename='enquiry')

urlpatterns = [
    path('show/', EnquiryViewSet.as_view({'get': 'list'}), name='enquiry-list'),
    path('create/', EnquiryViewSet.as_view({'post': 'create'}), name='enquiry-create'),
    path('<uuid:pk>/update/', EnquiryViewSet.as_view({'put': 'update'}), name='enquiry-update'),
    path('<uuid:pk>/delete/', EnquiryViewSet.as_view({'delete': 'destroy'}), name='enquiry-delete'),
]
