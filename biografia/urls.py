from django.contrib import admin
from django.urls import include, path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.biografia, name='biografia'),
    path('gravar/', views.gravar, name='gravar'),
    path('biografia/exibir/', views.exibe, name='exibe_convidados'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('atulizar/<int:id>', views.exibe, name='atualizar'),
    path('apagar/<int:id>', views.apagar, name='apagar'),
    path('accounts/', include('django.contrib.auth.urls')),

]