# core/services/veracode_sync_service.py

from ..gateways.veracode_gateway import VeracodeGateway
from ..mappers.workspace_mapper import WorkspaceMapper
from ..mappers.project_mapper import ProjectMapper
from ..mappers.scan_mapper import ScanMapper
from ..mappers.vulnerability_mapper import VulnerabilidadeMapper

from ..repositories.workspace_repository import WorkspaceRepository
from ..repositories.project_repository import ProjectRepository
from ..repositories.version_repository import VersionRepository
from ..repositories.scan_repository import ScanRepository
from ..repositories.vulnerability_repository import VulnerabilityRepository


class VeracodeSyncService:
    def __init__(self):
        self.gateway = VeracodeGateway()
        self.workspace_mapper = WorkspaceMapper()
        self.project_mapper = ProjectMapper()
        self.scan_mapper = ScanMapper()
        self.vuln_mapper = VulnerabilidadeMapper()

        self.workspace_repo = WorkspaceRepository()
        self.project_repo = ProjectRepository()
        self.version_repo = VersionRepository()
        self.scan_repo = ScanRepository()
        self.vulnerability_repo = VulnerabilityRepository()

    def sync_all_workspaces(self):
        raw_workspaces = self.gateway.list_workspaces().get("_embedded", [])
        for workspace_data in raw_workspaces:
            workspace_info = self.workspace_mapper.map(workspace_data)
            workspace = self.workspace_repo.get_or_create(**workspace_info)
            self.sync_workspace(workspace.workspace_id)

    def sync_workspace(self, workspace_id):
        raw_scans = self.gateway.list_sca_scans(workspace_id)
        workspace = self.workspace_repo.get_by_id(workspace_id)

        for scan_data in raw_scans:
            # Projeto
            project_info = self.project_mapper.map(scan_data.get("project"))
            projeto = self.project_repo.get_or_create(**project_info)

            # Versão
            numero_versao, data_geracao = self.scan_mapper.map_version_info(scan_data.get("version"))
            versao = None
            if numero_versao:
                versao = self.version_repo.get_or_create(numero=numero_versao, data_geracao=data_geracao)

            # Scan
            scan_fields = self.scan_mapper.map(scan_data)
            scan = self.scan_repo.get_or_create(
                scan_id_externo=scan_fields["scan_id_externo"],
                projeto=projeto,
                versao=versao,
                tipo=scan_fields["tipo"],
                ferramenta=scan_fields["ferramenta"],
                workspace=workspace
            )

            # Vulnerabilidades
            findings = self.gateway.get_sca_findings(scan_fields["scan_id_externo"])
            for finding in findings:
                vuln_data = self.vuln_mapper.map_from_veracode_issue(finding)
                self.vulnerability_repo.create(scan=scan, **vuln_data)

    def sync_project_by_name(self, target_name):
        raw_workspaces = self.gateway.list_workspaces().get("_embedded", [])
        for workspace_data in raw_workspaces:
            workspace_id = workspace_data["id"]
            raw_scans = self.gateway.list_sca_scans(workspace_id)
            for scan_data in raw_scans:
                project_name = self.scan_mapper.map_project_name(scan_data)
                if project_name and project_name.lower() == target_name.lower():
                    self.sync_workspace(workspace_id)
                    return