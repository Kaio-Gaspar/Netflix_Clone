
from .models import Conteudo_db


# conteudo/novos_context.py
from .models import Conteudo_db

def lista_conteudos_recentes(request):
    lista_conteudos = Conteudo_db.objects.all().order_by('data_criacao')
    return {"lista_conteudos_recentes": lista_conteudos}

def lista_conteudos_populares(request):
    lista_conteudos = Conteudo_db.objects.all().order_by('qnt_views')[:10]
    return {"lista_conteudos_populares": lista_conteudos}
