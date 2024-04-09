from django.urls import path, reverse_lazy
from .views import Homepage, Homeconteudo, Detalhesconteudo, Pesquisaconteudo, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_view

app_name = 'conteudo'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('conteudo/', Homeconteudo.as_view(), name='homeconteudo'),
    path('conteudo/<int:pk>/', Detalhesconteudo.as_view(), name='detalhesconteudo'),
    path('pesquisa/', Pesquisaconteudo.as_view(), name='pesquisaconteudos'),

    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),

    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),

    path('criarconta/', Criarconta.as_view(), name='criarconta'  ),

    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy('conteudo:homeconteudo')), name='mudarsenha'),



]
