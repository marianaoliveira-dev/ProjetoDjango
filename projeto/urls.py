from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('biografia.urls')),
    path('biografia/', include('biografia.urls')),
]
