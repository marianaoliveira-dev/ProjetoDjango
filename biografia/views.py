from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render

from biografia.models import Convidado

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

# from django.shortcuts import redirect, render
# from biografia.models import Convidado

# def biografia(request):
#     contexto = {
#         'titulo': 'ArteViva | Biografia'
#     }
#     return render(request, 'biografia/index.html', contexto)

# def gravar(request):
#     if request.method == "POST":
#         nome = request.POST.get("nome")
#         email = request.POST.get("email")
#         Convidado.objects.create(nome=nome, email=email)
#         return redirect("biografia")  # ou outra página

# def exibe(request):
#     # Exibir todos os convidados
#     exibe_pessoas = Convidado.objects.all()  # <-- Aqui também Convidado
#     return render(
#         request,
#         'biografia/mostrar.html',
#         {'pessoas': exibe_pessoas}
#     )