from django.contrib import admin
from django.db.models import Q
from .models import *

#Filtros

class UriComprobante(admin.SimpleListFilter):
	title = ('Comprobante')
	parameter_name = 'Imagen'

	def lookups(self, request, model_admin):
		return (
			('C', ('Con comprobante')),
			('V', ('Sin comprobante')),
		)

	def queryset(self, request, queryset):

		if self.value() == 'C':
			return queryset.filter(uri__isnull=False).exclude(uri='')
		if self.value() == 'V':
			return queryset.filter(Q(uri__isnull=True) | Q(uri__exact=''))

#AdminModels
class CompraModelAdmin(admin.ModelAdmin):
	list_display =('usuario','paquete','aprobada')
	list_filter = ('aprobada',UriComprobante)
# Register your models here.
admin.site.register(Tip)
admin.site.register(Concepto)
admin.site.register(Paquete)
admin.site.register(Compra,CompraModelAdmin)
admin.site.register(Video)
admin.site.register(Medicamento)
admin.site.register(Foto)
admin.site.register(Experiencia)
