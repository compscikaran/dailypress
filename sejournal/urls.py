
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.staticfiles.urls import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('authoring/', include('authoring.urls')),
    path('', include('presentation.urls')),
    path('accounts/', include('accounts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)