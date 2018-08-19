from .views import (FornecedoreListView, FornecedoreCreateView, FornecedoreDetailView,
                    FornecedoreUpdateView, FornecedoreDeleteView, handler404,
                    handler500, enviaremail)
from django.urls import path
from .apps import ControledefornecedoresConfig

app_name = ControledefornecedoresConfig.name

urlpatterns = [
    path('add/', FornecedoreCreateView.as_view(), name='add'),
    path('list', FornecedoreListView.as_view(), name='list'),
    path('<int:pk>/detail/', FornecedoreDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', FornecedoreUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', FornecedoreDeleteView.as_view(), name='delete'),
    path('email/', enviaremail, name='enviar-email'),
]

handler404 = handler404
handler500 = handler500