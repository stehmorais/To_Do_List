from django.contrib import admin
from .models import AtividadesModel

@admin.register(AtividadesModel)
class AtividadesModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dia', 'mes', 'modificado_em')
    list_editable = ('dia', 'mes')
    list_filter = ('dia', 'mes', 'modificado_em')

# usuario: admin
# senha: 123mudar