from django.contrib import admin
from .models import Categoria,Obra,Registo,Arquivo

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Obra)
admin.site.register(Registo)
admin.site.register(Arquivo)
