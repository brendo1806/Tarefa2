from django.db import models
class Produto(models.Model):
    codigo = models.CharField('Código',max_length=20,null=True,blank=True)
    descricao = models.CharField('Descrição',max_length=80,null=True,blank=True)
    valorunitario = models.DecimalField('Valor Unitário',decimal_places=2,max_digits=4,null=True,blank=True)
    quantidadedeestoque = models.DecimalField('Quantidade de Estoque',decimal_places=2,max_digits=4,null=True,blank=True)

    def __str__(self):
        return self.nome

