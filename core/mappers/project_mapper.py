class ProjectMapper:
    def map(self, data):
        return {
            "nome": data.get("name"),
            "status": "ativo"  # Pode adaptar se vier algum campo indicativo
        }