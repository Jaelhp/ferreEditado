# terceros/views.py
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Cliente, Proveedor

# --- Vistas para Clientes (CRUD) ---

class ClienteListView(ListView):
    model = Cliente
    template_name = 'terceros/cliente_list.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = '__all__' # Incluye todos los campos del modelo
    template_name = 'terceros/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'terceros/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

# --- Vistas para Proveedores (CRUD) ---

class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'terceros/proveedor_list.html'
    context_object_name = 'proveedores'

class ProveedorCreateView(CreateView):
    model = Proveedor
    fields = '__all__'
    template_name = 'terceros/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    fields = '__all__'
    template_name = 'terceros/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')