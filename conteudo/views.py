from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, reverse
from .models import Conteudo_db, Usuario
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import Criarcontaform, FormHome


# Create your views here.
#def homepage(request):
#   return render(request, "homepage.html")

class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHome

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('conteudo:homeconteudo')
        else:
            return super().get(request, *args, **kwargs) # redireciona para homepage

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('conteudo:login')
        else:
            return reverse('conteudo:criarconta')
        

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
    
class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('conteudo:homeconteudo')
        

class Criarconta(FormView):
    template_name = 'criarconta.html'
    form_class = Criarcontaform

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('conteudo:login')