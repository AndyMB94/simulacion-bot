from django.db import models

# Create your models here.

class BotData(models.Model):
    id = models.IntegerField(primary_key=True)  # ID manual
    idsig = models.IntegerField()
    tipo_doc = models.CharField(max_length=20)
    numero_doc = models.CharField(max_length=20)
    numero_tele = models.CharField(max_length=15)
    operadora = models.CharField(max_length=20)
    respuesta_bot = models.TextField()  # Para almacenar la respuesta generada

    def __str__(self):
        return f"ID: {self.id}, ID_SIG: {self.idsig}, Tipo: {self.tipo_doc}"
