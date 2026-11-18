from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Comida

class ComidaDetailView(DetailView):
    model = Comida
    template_name = 'comida_detail.html'

class ComidaListView(ListView):
    model = Comida
    template_name = 'comida_list.html'
    context_object_name = 'comidas'

    def get_queryset(self):
        return Comida.objects.select_related('categoria').all()

class ComidaCreateView(CreateView):
    model = Comida
    template_name = 'comida_form.html'
    fields = ['nombre', 'descripcion', 'precio', 'categoria']
    success_url = reverse_lazy('comida_list')

class ComidaUpdateView(UpdateView):
    model = Comida
    template_name = 'comida_form.html'
    fields = ['nombre', 'descripcion', 'precio', 'categoria']
    success_url = reverse_lazy('comida_list')

class ComidaDeleteView(DeleteView):
    model = Comida
    template_name = 'comida_confirm_delete.html'
    success_url = reverse_lazy('comida_list')