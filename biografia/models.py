from django.db import models
# Create your models here.
class Convidado(models.Model):
     id_pessoa = models.AutoField(primary_key=True),
     nome = models.TextField(max_length=100),
     email = models.EmailField(max_length=255),
