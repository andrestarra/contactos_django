from django.contrib import admin
from .models import Persona

# Para que el modelo Persona salga en el Admin Site
admin.site.register(Persona)
