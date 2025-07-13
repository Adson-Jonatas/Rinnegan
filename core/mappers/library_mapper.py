class LibraryMapper:
    def map(self, library):
        return {
            "nome": library.get("name"),
            "versao": library.get("version"),
            "transitiva": library.get("transitive", False),
            "direta": library.get("direct", False)
        }