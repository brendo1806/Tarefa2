# Generated by Django 2.0.7 on 2018-08-13 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nome')),
                ('CNPJ', models.PositiveIntegerField(blank=True, null=True, verbose_name='CNPJ')),
                ('endereco', models.CharField(blank=True, max_length=30, null=True, verbose_name='Endereço')),
                ('tipo', models.PositiveIntegerField(choices=[(1, 'Ativo'), (2, 'Inativo')], verbose_name='Tipo')),
                ('email', models.EmailField(blank=True, default='', max_length=30, null=True)),
                ('status', models.PositiveIntegerField(choices=[(0, 'Não Faturado'), (1, 'Faturado'), (2, 'Faturado e Enviado')], default=True, verbose_name='Status do Pedido')),
            ],
        ),
    ]
