# from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render

# Create your views here.
def biografia(request):
    contexto = {
        'titulo' : 'ArteViva | Biografia'
    }
    return render(request, 
                  'biografia/index.html',
                  contexto,
                  )
