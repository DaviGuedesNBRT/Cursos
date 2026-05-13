from django.contrib import admin
from .models import tb_categorias, tb_suario, tb_receitas
# Register your models here.

@admin.register(tb_categorias)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(tb_suario)
class UsuarioAdmin(admin.ModelAdmin):
    ...

@admin.register(tb_receitas)
class ReceitaAdmin(admin.ModelAdmin):
    ...


