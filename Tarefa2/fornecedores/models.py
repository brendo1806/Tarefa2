from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField('Nome', max_length=30, null=True,blank=True)
    CNPJ = models.PositiveIntegerField('CNPJ',null=True,blank=True)
    endereco = models.CharField('Endereço',max_length=30,null=True,blank=True)
    TIPO = ((1, 'Ativo'),(2, 'Inativo'))
    tipo = models.PositiveIntegerField(verbose_name='Tipo', choices= TIPO)
    email = models.EmailField(default='',max_length=30,null=True,blank=True)
    STATUS = ((0, 'Não Faturado'),(1, 'Faturado'),(2, 'Faturado e Enviado'))
    status = models.PositiveIntegerField(verbose_name='Status do Pedido',default=True, choices= STATUS)

    def __str__(self):
        return self.nome
