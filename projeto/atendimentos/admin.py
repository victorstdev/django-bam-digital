from django.contrib import admin
from .models import TipoAtendimento, Doenca
# Register your models here.

@admin.register(TipoAtendimento)
class TipoAtendimentoAdmin(admin.ModelAdmin):
  pass