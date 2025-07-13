from core.models import Workspace

class WorkspaceRepository:
    def get_or_create(self, workspace_id, nome, ferramenta):
        return Workspace.objects.get_or_create(
            workspace_id=workspace_id,
            defaults={"nome": nome, "ferramenta": ferramenta}
        )

    def get_by_id(self, workspace_id):
        return Workspace.objects.get(workspace_id=workspace_id)