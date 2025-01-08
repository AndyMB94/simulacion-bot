from django.contrib import admin
from .models import BotData

# Register your models here.

@admin.register(BotData)
class BotDataAdmin(admin.ModelAdmin):
    # Campos que se mostrarán como columnas en el panel de administración
    list_display = (
        'id', 
        'idsig', 
        'tipo_doc', 
        'numero_doc', 
        'numero_tele', 
        'operadora', 
        'respuesta_bot'
    )
    
    # Opciones de filtro en la barra lateral
    list_filter = ('tipo_doc', 'operadora')  
    
    # Campos que se pueden buscar
    search_fields = ('id', 'idsig', 'numero_doc', 'numero_tele')