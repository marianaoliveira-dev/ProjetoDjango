from django.shortcuts import render

from biografia.admin import ConvidadoAdmin
# Create your views here.
from .models import Convidado

# Create your views here.
def biografia(request):
    contexto = {
        'titulo' : 'ArteViva | Biografia',
        'convidados' : Convidado.objects.all()
    }
    return render(request, 
                  'biografia/index.html',
                  contexto
                  )

def gravar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')

        nova_pessoa = Convidado(nome=nome, email=email)
        nova_pessoa.save()

        convidados = Convidado.objects.all()
        # return render(request, 'biografia/index.html', {
        #     'convidados': convidados,
        #     'inscrito_sucesso': True
        # })
        
        # html_extra = "<p style='color: green;'>Cadastro realizado com sucesso!</p>"

        return render(request, 'biografia/index.html', {
            'convidados': convidados,
            'inscrito_sucesso': True,
            # 'html_extra': html_extra
        })

    # Se não for POST, apenas renderiza normalmente
    convidados = Convidado.objects.all()
    return render(request, 'biografia/index.html', {'convidados': convidados})


def exibe(request):
    convidados = Convidado.objects.all() #chama os dados do banco de dados
    print(f"{Convidado.objects.count()}")
    
    exibe_convidados = {
        'convidados': Convidado.objects.all()
    } 
    context = {
        'convidados': convidados
    }

    # retornar os dados para a página
    return render(
        request,
        '../base/global/partials/footer.html',
        context,
    )
    
def editar(request, id):
    convidados = Convidado.objects.get(id=id)
    return render(
        request,
        
    )

def atualizar(request, id):
    convidados = Convidado.objects.get(id=id)
    convidados.nome = request.POST.get('nome')
    convidados.email = request.POST.get('email')
    convidados.save()
    
    return exibe(request)

def apagar(request, id):
    convidados = Convidado.objects.get(id=id)
    convidados.delete()
    
    return exibe(request)