from django.db import models


class SiglaBase(models.Model):
    nome = models.CharField("Nome da Sigla Base", max_length=100, unique=True)

    class Meta:
        verbose_name = "Sigla Base"
        verbose_name_plural = "Siglas Base"

    def __str__(self):
        return self.nome
