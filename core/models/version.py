from django.db import models
from .branch import Branch


class Version(models.Model):
    numero = models.CharField("Número da Versão", max_length=50)
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name="versoes",
        verbose_name="Branch"
    )
    data_geracao = models.DateTimeField("Data de Geração", auto_now_add=True)

    class Meta:
        verbose_name = "Versão"
        verbose_name_plural = "Versões"

    def __str__(self):
        return f"{self.numero} ({self.branch.nome})"
