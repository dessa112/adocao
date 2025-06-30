from django.contrib import admin
from .models import (
    Cidade,
    Adotante,
    Adotado,
    Instituicao,
    Compatibilidade,
    ProcessoAdocao,
    Informativo,
    Administrador
)

admin.site.register(Cidade)
admin.site.register(Adotante)
admin.site.register(Adotado)
admin.site.register(Instituicao)
admin.site.register(Compatibilidade)
admin.site.register(ProcessoAdocao)
admin.site.register(Informativo)
admin.site.register(Administrador)