from core.models import Scan


class ScanRepository:
    def get_or_create(self, scan_id_externo, projeto, versao, tipo, ferramenta, workspace):
        return Scan.objects.get_or_create(
            scan_id_externo=scan_id_externo,
            defaults={
                "projeto": projeto,
                "versao": versao,
                "tipo": tipo,
                "ferramenta": ferramenta,
                "workspace": workspace
            }
        )