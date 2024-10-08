from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

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
    path('api/products/', include('product.urls')),
    path('api/category/', include('category.urls')),
    path('api/brand/', include('brands.urls')),
    path('api/color/', include('colors.urls')),
    path('api/enquiry/', include('Enquiry.urls')),
    path('api/payments/', include('payments.urls')),
<<<<<<< HEAD
    path('api/uploads/', include('FileUpload.urls')),
    # path('api/fileupload/', include(fileupload_router.urls)),
=======
    path('api/location/', include('locations.urls')),
    path('api/uploads/', include('FileUpload.urls')),  # Include FileUpload app URLs
    path('api/', include(fileupload_router.urls)),  # Register FileUploadViewSet with DefaultRouter
    
>>>>>>> 31e0ec9990aab156c7edc73020858bc384bc2f67
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)