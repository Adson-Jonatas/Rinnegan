class ScanMapper:
    def map(self, data):
        return {
            "scan_id_externo": data.get("id"),
            "tipo": data.get("type", "SCA"),
            "ferramenta": data.get("tool", "Veracode"),
            "data_execucao": data.get("date")
        }

    def map_branch_info(self, data):
        return {
            "branch": data.get("branch"),
            "commit": data.get("commit"),
            "tag": data.get("tag")
        }

    def map_version_info(self, version_data):
        if not version_data:
            return None, None
        return version_data.get("number"), version_data.get("created_at")

    def map_project_name(self, data):
        return data.get("project", {}).get("name")