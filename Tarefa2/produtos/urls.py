from .views import (ProdutoDeleteView, ProdutoDetailView, ProdutoUpdateView,
                    ProdutoCreateView, ProdutoListView)
from django.urls import path
from .apps import ProdutosConfig

app_name = ProdutosConfig.name
urlpatterns = [
    path('', ProdutoListView.as_view(), name='list'),
    path('add/', ProdutoCreateView.as_view(), name='add'),
    path('<int:pk>/detail/', ProdutoDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', ProdutoUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', ProdutoDeleteView.as_view(), name='delete')


]
