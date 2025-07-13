from core.models import Version


class VersionRepository:
    def get_or_create(self, numero, data_geracao):
        return Version.objects.get_or_create(
            numero=numero,
            defaults={"data_geracao": data_geracao}
        )