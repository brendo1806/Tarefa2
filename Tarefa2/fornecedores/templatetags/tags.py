from django import template
from Tarefa2.fornecedores.models import Fornecedor


register = template.Library()

@register.filter
def tipo_choices(value):
    return dict(Fornecedor.TIPO).get(value, "")
