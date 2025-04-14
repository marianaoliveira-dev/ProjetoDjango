from django.contrib import admin
from django.urls import path, include
from biografia import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.biografia, name='biografia'),
]

urlpatterns = [
    path('', views.biografia, name='biografia'),
    path('gravar/', views.gravar, name='gravar'),
]