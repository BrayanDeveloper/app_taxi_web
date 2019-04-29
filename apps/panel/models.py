from django.db import models
from datetime import datetime
# Create your models here.

from django.db import models
from datetime import datetime 
# Create your models here.

class Solicitud_de_llamadas(models.Model):
    titulo = models.CharField(max_length=30)
    codigo = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=30)
    porcentaje_descuento = models.CharField(max_length=30)
    descuento_plano = models.CharField(max_length=30)
    inicio = models.DateField(default=datetime.now())
    expiration = models.DateField(default=datetime.now())
    fecha = models.DateField(default=datetime.now())

class Quejas(models.Model):
    fecha_hora = models.DateTimeField()
    de = models.CharField(max_length=30)
    tipo = models.TextField(max_length=30)
    tema = models.CharField(max_length=30)
    contenido = models.CharField(max_length=30)
    fecha = models.DateField(default=datetime.now())

class Solicitud_de_pagos(models.Model):
    nombre_conductor = models.CharField(max_length=30)
    numero_conductor = models.CharField(max_length=30)
    fecha_solicitud = models.DateField(default=datetime.now())
    fecha_pago = models.DateField(default=datetime.now())
    monto = models.CharField(max_length=30)
    numero_cuenta = models.CharField(max_length=30)
    comentario = models.TextField(max_length=5000)
    fecha = models.DateField(default=datetime.now())

class Cupones(models.Model):
    titulo = models.CharField(max_length=30)
    codigo = models.CharField(max_length=30)
    imagen_cupon = models.ImageField(upload_to="static/img/images_cupones/")
    descripcion = models.TextField(max_length=30)
    porcentaje_descuento = models.CharField(max_length=30)
    descuento_plano = models.CharField(max_length=30)
    inicio = models.DateField(default=datetime.now())
    expiration = models.DateField(default=datetime.now())
    fecha = models.DateField(default=datetime.now())

class Conductores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    imagen_conductor = models.ImageField(upload_to="static/img/images_conductores/")
    numero_certificado = models.TextField(max_length=30)
    numero_celular = models.CharField(max_length=30)
    raiting = models.CharField(max_length=30)
    placa_carro = models.CharField(max_length=30)
    fecha = models.DateField(default=datetime.now())


class Pasajeros(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    imagen_pasajero = models.ImageField(upload_to="static/img/images_pasajeros/")
    numero_certificado = models.TextField(max_length=30)
    numero_celular = models.CharField(max_length=30)
    balance = models.CharField(max_length=30)
    direccion = models.CharField(max_length=300)
    fecha = models.DateField(default=datetime.now())

class Promociones(models.Model):
    titulo = models.CharField(max_length=30)
    imagen_promocion = models.ImageField(upload_to="static/img/images_promociones/")
    inicio = models.DateField(default=datetime.now())
    fin = models.DateField(default=datetime.now())
    descripcion = models.TextField(max_length=30)
    fecha = models.DateField(default=datetime.now())

class Viajes(models.Model):
    direccion_inicio = models.CharField(max_length=3000)
    direccion_destino = models.CharField(max_length=3000)
    raiting = models.TextField(max_length=30)
    fecha = models.DateField(default=datetime.now())