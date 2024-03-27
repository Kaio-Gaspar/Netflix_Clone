from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, reverse
from .models import Conteudo_db
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import Criarcontaform


# Create your views here.
#def homepage(request):
#   return render(request, "homepage.html")

class Homepage(TemplateView):
    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('conteudo:homeconteudo')
        else:
            return super().get(request, *args, **kwargs) # redireciona para homepage

class Homeconteudo(LoginRequiredMixin, ListView):
    template_name = 'homeconteudo.html'
    model = Conteudo_db

class Detalhesconteudo(LoginRequiredMixin, DetailView):
    template_name = 'detalhesconteudo.html'
    model = Conteudo_db

    def get(self, request, *args, **kwargs):
        #contabilizar visualizações
        conteudo = self.get_object()
        conteudo.qnt_views += 1
        conteudo.save()
        usuario = request.user
        usuario.conteudos_vistos.add(conteudo)
        return super().get(request, *args, **kwargs) #redireciona o usuario para o url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesconteudo, self).get_context_data(**kwargs)

        conteudos_relacionados = Conteudo_db.objects.filter(categoria=self.get_object().categoria)[0:5]

        context['conteudos_relacionados'] = conteudos_relacionados
        return context

class Pesquisaconteudo(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Conteudo_db

    def get_queryset(self) -> QuerySet[Any]:
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list =  Conteudo_db.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None
        return super().get_queryset()
    
class Paginaperfil(LoginRequiredMixin, TemplateView):
    template_name = 'editarperfil.html'

class Criarconta(FormView):
    template_name = 'criarconta.html'
    form_class = Criarcontaform

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('conteudo:login')