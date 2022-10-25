from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Equipo(models.Model):
    referencia = models.CharField('Referencia', max_length=100)
    marca = models.CharField('Marca', max_length=100)
    procesador = models.CharField('Procesador', max_length=100)
    memoria = models.CharField('Memoria', max_length=100)
    disco = models.CharField('Disco', max_length=100)
    tipo = models.CharField('Tipo', max_length=100)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __str__(self):
        return self.referencia

class EquipoUsuario(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    fecha_asignacion = models.DateField('Fecha de asignación', auto_now_add=True)
    fecha_entrega = models.DateField('Fecha de entrega', blank=True, null=True)

    class Meta:

        verbose_name = 'Equipo Usuario'
        verbose_name_plural = 'Equipos Usuarios'

    def __str__(self):
        return self.equipo.referencia + " - " + self.usuario.username

