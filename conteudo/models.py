from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

LISTA_CATEGORIAS = (
("analises", "Análises"),
("PROGRAMACAO", "Programação"),
("APRESENTACAO", "Apresentação"),
("OUTROS", "Outros")
)

#criar filmes
class Conteudo_db(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_conteudo/')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    qnt_views = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.titulo
#criar episodios
    

class Episodio(models.Model):
    Conteudo_db = models.ForeignKey('conteudo_db', related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.titulo

class Usuario(AbstractUser):
    conteudos_vistos = models.ManyToManyField("Conteudo_db")