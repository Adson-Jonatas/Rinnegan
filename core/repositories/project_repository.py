from core.models import Project


class ProjectRepository:
    def get_or_create(self, nome):
        return Project.objects.get_or_create(nome=nome)

    def get_by_nome(self, nome):
        return Project.objects.filter(nome__iexact=nome).first()