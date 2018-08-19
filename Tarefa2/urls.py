from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fornecedores/', include('Tarefa2.fornecedores.urls', namespace='fornecedores')),
    path('produtos', include('Tarefa2.produtos.urls', namespace='produtos')),
    path('', TemplateView.as_view(template_name="index.html"))
]
