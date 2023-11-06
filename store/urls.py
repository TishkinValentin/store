from django.contrib import admin
from django.urls import path, include
from products.views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)