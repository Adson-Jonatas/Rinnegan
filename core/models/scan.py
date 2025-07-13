from django.db import models
from core.models.project import Project
from core.models.version import Version
from .workspace_sca_veracode import Workspace


class TipoScan(models.TextChoices):
    SAST = "SAST", "SAST"
    SCA = "SCA", "SCA"
    IMAGE = "IMAGE", "Imagem"

class Scan(models.Model):
    projeto = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="scans",
        verbose_name="Projeto"
    )
    versao = models.ForeignKey(
        Version,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="scans",
        verbose_name="Versão"
    )
    tipo = models.CharField(
        "Tipo de Scan",
        max_length=20,
        choices=TipoScan.choices
    )
    ferramenta = models.CharField("Ferramenta", max_length=100)
    data_execucao = models.DateTimeField("Data de Execução", auto_now_add=True)
    scan_id_externo = models.CharField("ID Externo do Scan", max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Scan"
        verbose_name_plural = "Scans"

    def __str__(self):
        return f"{self.tipo} - {self.projeto.nome} - {self.data_execucao.strftime('%Y-%m-%d %H:%M')}"
