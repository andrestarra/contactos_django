from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView # View
from django.urls import reverse_lazy
from .forms import PersonaForm
from .models import Persona

"""
class ListView(View):
    model = Persona
    template_ name = 'index.html'

    def dispatch()

    def get_context_data(self):
        context = {}
        context['queryset'] = self.get_queryset()
        return context

    def get_queryset(self):
        return self.model.objects.all()

    def get_templates_names():
        return self.template_name

    def get(self, request, *args, **kwargs):
        return render(request, self.get_templates_names(), self.get_context_data())
"""

class PersonaList(ListView):
    model = Persona
    template_name = 'index.html'

#    def get_queryset(self):
#       return self.model.objects.all()[:2]

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')
