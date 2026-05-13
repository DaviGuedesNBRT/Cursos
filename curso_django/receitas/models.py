from django.db import models


class tb_categorias(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_nome = models.CharField(max_length=255)

    def __str__(self):
        return self.cat_nome


class tb_suario(models.Model):
    usu_id = models.AutoField(primary_key=True)
    usu_nome = models.CharField(max_length=255)
    usu_email = models.EmailField(unique=True)
    usu_senha = models.CharField(max_length=255)

    def __str__(self):
        return self.usu_nome


class tb_receitas(models.Model):
    rec_id = models.AutoField(primary_key=True)
    rec_nome = models.CharField(max_length=255)
    rec_descricao = models.TextField()
    rec_ingredientes = models.TextField()
    rec_modo_preparo = models.TextField()
    rec_tempo_preparo = models.IntegerField()
    rec_rendimento = models.IntegerField()

    rec_categoria = models.ForeignKey(
        tb_categorias,
        on_delete=models.SET_NULL, null=True
    )

    rec_imagem = models.ImageField(
        upload_to='receitas/imagens/'
    )

    rec_data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    rec_user_id = models.ForeignKey(
        tb_suario,
        on_delete=models.SET_NULL, null=True
    )

    rec_data_atualizacao = models.DateTimeField(
        auto_now=True
    )

    rec_publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.rec_nome