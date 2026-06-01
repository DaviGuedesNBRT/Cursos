from django.db import models
from django.contrib.auth.models import User  # Usar o User do Django

class tb_categorias(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.cat_nome

class tb_receitas(models.Model):
    rec_id = models.AutoField(primary_key=True)
    rec_nome = models.CharField(max_length=255)
    rec_descricao = models.TextField()
    rec_ingredientes = models.TextField()
    rec_modo_preparo = models.TextField()
    rec_tempo_preparo = models.IntegerField()
    rec_rendimento = models.IntegerField()
    
    rec_categoria = models.ForeignKey(tb_categorias, on_delete=models.SET_NULL, null=True, blank=True, default=None) 
    rec_imagem = models.ImageField(upload_to='receitas/imagens/')
    rec_data_criacao = models.DateTimeField(auto_now_add=True)
    
    # Mudar para User do Django
    rec_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    rec_data_atualizacao = models.DateTimeField(auto_now=True)
    rec_publicada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.rec_nome
    

class tb_favoritos(models.Model):
    fav_id = models.AutoField(primary_key=True)
    fav_user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacionamento com User do Django
    fav_receita_id = models.ForeignKey(tb_receitas, on_delete=models.CASCADE)  # Relacionamento com tb_receitas
    fav_data_adicao = models.DateTimeField(auto_now_add=True)

    class meta:
        unique_together = ('fav_user_id', 'fav_receita_id') 
    
    def __str__(self):
        return f"{self.fav_user_id.username} - {self.fav_receita_id.rec_nome}"