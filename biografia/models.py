from django.db import models
# Create your models here.
class Convidado(models.Model):
     nome = models.CharField(max_length=100)
     email = models.EmailField(max_length=255)

     def __str__(self):
          return f'{self.nome} acaba de ser cadastrado!' #é uma função pra confirmar se foi cadastrado
