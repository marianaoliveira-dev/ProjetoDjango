# from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render

from biografia.models import Pessoa

# Create your views here.
def biografia(request):
    contexto = {
        'titulo' : 'ArteViva | Biografia'
    }
    return render(request, 
                  'biografia/index.html',
                  contexto,
                  )

def gravar(request):
    # Salvar os dados da tela para o banco
    nova_pessoa = Pessoa()
    nova_pessoa.nome = request.POST.get('nome')
    nova_pessoa.email = request.POST.get('email')
    nova_pessoa.save()
    
    return biografia(request)

def exibe(request):
    # exibir todas as pessoas
    exibe_pessoas = {
        'pessoas': Pessoa.objects.all()
    }
    # retornar os dados para a página
    return render(
        request,
        'biografia/mostrar.html',
        exibe_pessoas,
    )