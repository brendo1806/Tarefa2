from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Produto
from .forms import ProdutoForm
from django.urls import reverse_lazy
from django.shortcuts import render

class ProdutoListView(ListView):
    def get_context_object_name(self, object_list):
        return 'listp'
    def get_template_names(self):
        return 'produto_list.html'
    def get_queryset(self):
        return Produto.objects.all()

class ProdutoCreateView(CreateView):
    model = Produto
    def get_template_names(self):
        return'produto_form.html'
    def get_success_url(self):
        return reverse_lazy('produto:list')
    def get_form_class(self):
        return ProdutoForm

class ProdutoUpdateView(UpdateView):
    model = Produto
    def get_template_names(self):
        return'produto_form.html'
    def get_success_url(self):
        return reverse_lazy('produto:list')
    def get_form_class(self):
        return ProdutoForm


class ProdutoDetailView(DetailView):
    model = Produto
    def get_template_names(self):
        return 'produto_detail.html'

class ProdutoDeleteView(DeleteView):
    model = Produto
    def get_template_names(self):
        return 'produto_confim_delete.html'
    def get_success_url(self):
        return reverse_lazy('produto:list')