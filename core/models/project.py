from django.db import models
from .sigla_base import SiglaBase
from .sigla_modulo import SiglaModulo


class ProjetoStatus(models.TextChoices):
    ATIVO = 'ativo', 'Ativo'
    DESATIVADO = 'desativado', 'Desativado'

class Project(models.Model):
    nome = models.CharField("Nome do Projeto", max_length=100)
    sigla_base = models.ForeignKey(
        SiglaBase,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projetos',
        verbose_name="Sigla Base"
    )
    sigla_modulo = models.ForeignKey(
        SiglaModulo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projetos',
        verbose_name="Sigla Módulo"
    )
    status = models.CharField(
        "Status do Projeto",
        max_length=20,
        choices=ProjetoStatus.choices,
        default=ProjetoStatus.ATIVO
    )

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.nome
