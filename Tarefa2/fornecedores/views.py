from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Fornecedor
from .forms import FornecedorForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.mail import send_mail



class FornecedoreListView(ListView):
    def get_context_object_name(self, object_list):
        return 'controle_list'

    def get_template_names(self):
        return 'fornecedor_list.html'

    def get_queryset(self):
        return Fornecedor.objects.all()


class FornecedoreCreateView(CreateView):
    model = Fornecedor

    def get_template_names(self):
        return 'fornecedor_form.html'

    def get_success_url(self):
        return reverse_lazy('fornecedores:list')

    def get_form_class(self):
        return FornecedorForm


class FornecedoreUpdateView(UpdateView):
    model = Fornecedor

    def get_template_names(self):
        return 'fornecedor_form.html'

    def get_success_url(self):
        return reverse_lazy('fornecedores:list')

    def get_form_class(self):
        return FornecedorForm


class FornecedoreDetailView(DetailView):
    model = Fornecedor

    def get_template_names(self):
        return 'fornecedor_detail.html'


class FornecedoreDeleteView(DeleteView):
    model = Fornecedor

    def get_template_names(self):
        return 'fornecedor_confim_delete.html'

    def get_success_url(self):
        return reverse_lazy('fornecedores:list')


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


def enviaremail(request):
    send_mail(
        subject='Assunto:',
        message='Pedido realizado com sucesso.',
        from_email='de@example.com',
        recipient_list=['para@example.com'],
        fail_silently=False,
    )
    return HttpResponseRedirect(reverse_lazy('fornecedores:list'))



