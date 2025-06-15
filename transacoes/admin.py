from django.contrib import admin
from .models import Fonte, Transacao

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]

@admin.register(Fonte)
class FonteAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]