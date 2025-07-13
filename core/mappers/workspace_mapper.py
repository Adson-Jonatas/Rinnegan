class WorkspaceMapper:
    def map(self, data):
        return {
            "workspace_id": data.get("id"),
            "nome": data.get("name"),
            "ferramenta": "Veracode"
        }