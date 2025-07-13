from .veracode_sync_service import VeracodeSyncService


class ScanService:
    def __init__(self):
        self.veracode = VeracodeSyncService()

    def sync_todos_os_workspaces(self):
        self.veracode.sync_all_workspaces()

    def sync_workspace(self, workspace_id):
        self.veracode.sync_workspace(workspace_id)

    def sync_projeto_por_nome(self, nome_projeto):
        self.veracode.sync_project_by_name(nome_projeto)