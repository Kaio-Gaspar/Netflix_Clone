
from .models import Conteudo_db


# conteudo/novos_context.py
from .models import Conteudo_db

def lista_conteudos_recentes(request):
    lista_conteudos = Conteudo_db.objects.all().order_by('data_criacao')[0:8]
    if lista_conteudos:
        conteudo_destaque = lista_conteudos[0]
    else:
        conteudo_destaque = None
    return {"lista_conteudos_recentes": lista_conteudos, "conteudo_destaque": conteudo_destaque}

def lista_conteudos_populares(request):
    lista_conteudos = Conteudo_db.objects.all().order_by('qnt_views')[0:8]
    return {"lista_conteudos_populares": lista_conteudos}

