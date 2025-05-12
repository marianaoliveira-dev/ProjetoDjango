from django.contrib import admin
from biografia import models

# Register your models here.
@admin.register(models.Convidado)
class ConvidadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email',)