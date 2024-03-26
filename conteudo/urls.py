from django.urls import path
from .views import Homepage, Homeconteudo, Detalhesconteudo, Pesquisaconteudo
from django.contrib.auth import views as auth_view

app_name = 'conteudo'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('conteudo/', Homeconteudo.as_view(), name='homeconteudo'),
    path('conteudo/<int:pk>/', Detalhesconteudo.as_view(), name='detalhesconteudo'),
    path('pesquisa/', Pesquisaconteudo.as_view(), name='pesquisaconteudos'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout')



]
