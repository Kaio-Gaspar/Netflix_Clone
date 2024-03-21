from django.contrib import admin
from.models import Conteudo_db, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin


# Register your models here.

campos = list(UserAdmin.fieldsets)
campos.append(('Histórico', {'fields': ('conteudos_vistos',)}))

UserAdmin.fieldsets = tuple(campos)
admin.site.register(Conteudo_db)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)

