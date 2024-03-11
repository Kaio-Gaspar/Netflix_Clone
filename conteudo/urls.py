from django.urls import path
from .views import Homepage, Homeconteudo, Detalhesconteudo

app_name = 'conteudo'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('conteudo/', Homeconteudo.as_view(), name='homeconteudo'),
    path('conteudo/<int:pk>/', Detalhesconteudo.as_view(), name='detalhesconteudo')

]
