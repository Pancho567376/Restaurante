from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Comida
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class ComidaDetailView(DetailView):
    model = Comida
    template_name = 'comida_detail.html'

class ComidaListView(ListView):
    model = Comida
    template_name = 'comida_list.html'
    context_object_name = 'comidas'

    def get_queryset(self):
        return Comida.objects.select_related('categoria').all()

class ComidaCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Comida
    template_name = 'comida_form.html'
    fields = ['nombre', 'descripcion', 'precio', 'categoria']
    success_url = reverse_lazy('comida_list')
    success_message = 'Comida creada exitosamente.'

class ComidaUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Comida
    template_name = 'comida_form.html'
    fields = ['nombre', 'descripcion', 'precio', 'categoria']
    success_url = reverse_lazy('comida_list')
    success_message = 'Comida actualizada exitosamente.'

class ComidaDeleteView(LoginRequiredMixin, DeleteView):
    model = Comida
    template_name = 'comida_confirm_delete.html'
    success_url = reverse_lazy('comida_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, f'La comida "{self.object.nombre}" ha sido eliminada exitosamente.')
        response = super().delete(request, *args, **kwargs)

def detalle_comida(request, id):
    comida = get_object_or_404(Comida, id=id)
    contexto = {
        'comida': comida
    }
    return render(request, 'templates/comida_detail.html', contexto)