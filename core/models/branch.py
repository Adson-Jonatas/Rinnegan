from django.db import models
from core.models.project import Project


class Branch(models.Model):
    nome = models.CharField("Nome da Branch", max_length=100)
    projeto = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="branches",
        verbose_name="Projeto"
    )
    padrao = models.BooleanField("É padrão?", default=False)

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    def __str__(self):
        return f"{self.nome} ({self.projeto.nome})"

