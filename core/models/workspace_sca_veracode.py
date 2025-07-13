from django.db import models
from .project import Project


class Workspace(models.Model):
    nome = models.CharField("Nome do Workspace", max_length=100)
    ferramenta = models.CharField("Ferramenta", max_length=100)
    workspace_id = models.CharField("ID do Workspace", max_length=200)
    projeto = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="workspaces",
        verbose_name="Projeto"
    )

    class Meta:
        verbose_name = "Workspace"
        verbose_name_plural = "Workspaces"

    def __str__(self):
        return f"{self.nome} ({self.ferramenta})"
