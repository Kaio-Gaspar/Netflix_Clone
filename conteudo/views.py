from typing import Any
from django.shortcuts import render
from .models import Conteudo_db
from django.views.generic import TemplateView, ListView, DetailView



# Create your views here.
#def homepage(request):
#   return render(request, "homepage.html")

class Homepage(TemplateView):
    template_name = "homepage.html"


class Homeconteudo(ListView):
    template_name = 'homeconteudo.html'
    model = Conteudo_db

class Detalhesconteudo(DetailView):
    template_name = 'detalhesconteudo.html'
    model = Conteudo_db

    def get(self, request, *args, **kwargs):
        #contabilizar visualizações
        conteudo = self.get_object()
        conteudo.qnt_views += 1
        conteudo.save()
        return super().get(request, *args, **kwargs) #redireciona o usuario para o url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesconteudo, self).get_context_data(**kwargs)

        conteudos_relacionados = Conteudo_db.objects.filter(categoria=self.get_object().categoria)

        context['conteudos_relacionados'] = conteudos_relacionados
        return context
