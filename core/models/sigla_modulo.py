from django.db import models
from .sigla_base import SiglaBase


class SiglaModulo(models.Model):
    nome = models.CharField("Nome da Sigla Módulo", max_length=100, unique=True)
    sigla_base = models.ForeignKey(
        SiglaBase,
        on_delete=models.CASCADE,
        related_name='modulos',
        verbose_name="Sigla Base"
    )

    class Meta:
        verbose_name = "Sigla Módulo"
        verbose_name_plural = "Siglas Módulo"

    def __str__(self):
        return self.nome

