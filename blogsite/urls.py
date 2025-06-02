from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from gallery.views import CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gallery.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
