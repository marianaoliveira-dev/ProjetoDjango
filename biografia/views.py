from django.shortcuts import render
# Create your views here.
from .models import Convidado

# Create your views here.
def biografia(request):
    contexto = {
        'titulo' : 'ArteViva | Biografia'
    }
    return render(request, 
                  'biografia/index.html',
                  contexto
                  )

def gravar(request):
    # Salvar os dados da tela para o banco
    nova_pessoa = Convidado()
    nova_pessoa.nome = request.POST.get('nome')
    nova_pessoa.email = request.POST.get('email')
    nova_pessoa.save()
    
    return biografia(request)

def exibe(request):
    # exibir todas as pessoas
    exibe_pessoas = {
        'pessoas': Convidado.objects.all()
    }
    # retornar os dados para a página
    return render(
        request,
        'biografia/mostrar.html',
        exibe_pessoas,
    )