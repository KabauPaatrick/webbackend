# webbackend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from FileUpload.urls import router as fileupload_router

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/chat/', include('socials.urls')),
    path('api/tickets/', include('tickets.urls')),
    path('api/comments/', include('comments.urls')),
    path('api/customer/', include('customer.urls')),
    path('api/achievement/', include('achievemets.urls')),
    path('api/entity/', include('entity.urls')),
    path('api/solutions/', include('solutions.urls')),
    path('api/heropage/', include('HeroPage.urls')),
    path('api/homeview/', include('Homeview.urls')),
    path('api/testimonials/', include('testimonials.urls')),
    path('api/license/', include('license.urls')),
    path('api/users/', include('users.urls')),
    path('api/', include('login.urls')),
    # path('api/', include('logo.urls')),
    path('api/products/', include('product.urls')),
    path('api/category/', include('category.urls')),
    path('api/brand/', include('brands.urls')),
    path('api/color/', include('colors.urls')),
    path('api/enquiry/', include('Enquiry.urls')),
    path('api/payments/', include('payments.urls')),
    
    path('api/uploads/', include('FileUpload.urls')),  # Include FileUpload app URLs
    path('api/', include(fileupload_router.urls)),  # Register FileUploadViewSet with DefaultRouter
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
