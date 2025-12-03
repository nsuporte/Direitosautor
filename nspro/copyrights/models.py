from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=20)

    def __str__(self):
        return self.categoria


class Obra(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='obras')
    titulo = models.CharField(max_length=300,null=False,unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,related_name='obras')
    descricao = models.TextField(max_length=600)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Registo(models.Model):
    ESCOLHA_ESTADO = {
        ("PENDENTE","Pendente"),
        ("APROVADO","Aprovado"),
        ("REJEITADO","Rejeitado"),
    }
    obra = models.ForeignKey(Obra,on_delete=models.CASCADE, related_name='registos')
    numero_registo = models.CharField(max_length=10,unique=True,null=True)
    estado = models.CharField(max_length=10,choices=ESCOLHA_ESTADO,default="PENDENTE")
    criado_em = models.DateTimeField(auto_now_add=True)
    nota = models.TextField(max_length=600)

    agente = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='agente_registrador')

    def __str__(self):
        return f"Registo {self.numero_registo} - {self.obra.titulo}"

class Arquivo(models.Model):
    registo = models.ForeignKey(Registo,on_delete=models.CASCADE,related_name='arquivos')
    arquivo = models.FileField(upload_to="arquivo")
    actualizado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Arquivo do registo {self.registo.numero_registo}"
    