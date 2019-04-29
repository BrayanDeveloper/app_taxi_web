from django.contrib import admin
from apps.panel.models import *
# Register your models here.

class DisplaySolicitudLlamadas(admin.ModelAdmin):
    list_display = ['titulo','codigo','descripcion','porcentaje_descuento','descuento_plano','inicio','expiration','fecha']
    list_filter = ['titulo', 'codigo']
    search_fields = ['titulo', 'codigo']

class DisplayQuejas(admin.ModelAdmin):
    list_display = ['fecha_hora','de','tipo','tema','contenido','fecha']
    list_filter = ['fecha_hora', 'de']
    search_fields = ['titulo', 'de']

class DisplaySolicitudPagos(admin.ModelAdmin):
    list_display = ['nombre_conductor','numero_conductor','fecha_solicitud','fecha_pago','monto','numero_cuenta','comentario','fecha']
    list_filter = ['nombre_conductor', 'numero_conductor']
    search_fields = ['nombre_conductor', 'numero_conductor']

class DisplayCupones(admin.ModelAdmin):
    list_display = ['titulo','codigo','imagen_cupon','descripcion','porcentaje_descuento','descuento_plano','inicio','expiration','fecha']
    list_filter = ['titulo', 'codigo']
    search_fields = ['titulo', 'codigo']

class DisplayConductores(admin.ModelAdmin):
    list_display = ['nombre','apellido','numero_certificado','numero_celular','raiting','placa_carro','placa_carro']
    list_filter = ['nombre', 'apellido','numero_certificado']
    search_fields = ['nombre', 'apellido']

class DisplayPasajeros(admin.ModelAdmin):
    list_display = ['nombre','apellido','numero_certificado','numero_celular','balance','direccion','fecha']
    list_filter = ['nombre', 'apellido','numero_certificado']
    search_fields = ['nombre', 'apellido']

class DisplayPromociones(admin.ModelAdmin):
    list_display = ['titulo','inicio','fin','descripcion','fecha']
    list_filter = ['titulo', 'inicio']
    search_fields = ['titulo', 'inicio']

class DisplayViajes(admin.ModelAdmin):
    list_display = ['direccion_inicio','direccion_destino','raiting','fecha']
    list_filter = ['direccion_inicio', 'direccion_destino']
    search_fields = ['direccion_inicio', 'direccion_destino']

admin.site.register(Solicitud_de_llamadas,DisplaySolicitudLlamadas)
admin.site.register(Quejas,DisplayQuejas)
admin.site.register(Solicitud_de_pagos,DisplaySolicitudPagos)
admin.site.register(Cupones,DisplayCupones)
admin.site.register(Conductores,DisplayConductores)
admin.site.register(Pasajeros,DisplayPasajeros)
admin.site.register(Promociones,DisplayPromociones)
admin.site.register(Viajes,DisplayViajes)