from django.contrib import admin
from .models import Categoria_comidas, Comida

class Categoria_comidasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

class ComidaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'categoria')
    list_filter = ('categoria',)

admin.site.register(Categoria_comidas, Categoria_comidasAdmin)
admin.site.register(Comida, ComidaAdmin)
