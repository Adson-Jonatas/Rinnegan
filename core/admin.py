from django.contrib import admin
from .models.project import Project
from .models.sigla_base import SiglaBase
from .models.sigla_modulo import SiglaModulo
from .models.branch import Branch
from .models.version import Version
from .models.scan import Scan
from .models.workspace_sca_veracode import Workspace
from .models.vulnerability import Vulnerability
from django.contrib import messages
from .services.scan_service import ScanService


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla_base", "sigla_modulo", "status")
    search_fields = ("nome",)
    list_filter = ("status", "sigla_base", "sigla_modulo")
    ordering = ("nome",)
    readonly_fields = ("total_branches", "total_scans", "total_vulnerabilidades")

    def total_branches(self, obj):
        return obj.branches.count()

    def total_scans(self, obj):
        return obj.scans.count()

    def total_vulnerabilidades(self, obj):
        return sum(scan.vulnerabilidades.count() for scan in obj.scans.all())

    total_branches.short_description = "Branches"
    total_scans.short_description = "Scans"
    total_vulnerabilidades.short_description = "Vulnerabilidades"


@admin.register(SiglaBase)
class SiglaBaseAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(SiglaModulo)
class SiglaModuloAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla_base")
    search_fields = ("nome",)
    list_filter = ("sigla_base",)


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ("nome", "projeto", "padrao")
    search_fields = ("nome", "projeto__nome")
    list_filter = ("padrao", "projeto")


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("numero", "branch", "data_geracao")
    search_fields = ("numero", "branch__nome")
    list_filter = ("branch__projeto",)


@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_display = ("tipo", "ferramenta", "projeto", "versao", "data_execucao")
    search_fields = ("ferramenta", "projeto__nome", "scan_id_externo")
    list_filter = ("tipo", "ferramenta", "projeto")


@admin.action(description="🔄 Sincronizar Workspace com Veracode")
def sync_workspace_action(modeladmin, request, queryset):
    service = ScanService()
    for workspace in queryset:
        service.sync_workspace(workspace.workspace_id)
        messages.success(request, f"Workspace '{workspace.nome}' sincronizado com sucesso.")


@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ("nome", "ferramenta", "workspace_id", "projeto")
    search_fields = ("nome", "workspace_id", "projeto__nome")
    list_filter = ("ferramenta", "projeto")
    actions = [sync_workspace_action]  # 👈 aqui!


@admin.register(Vulnerability)
class VulnerabilidadeAdmin(admin.ModelAdmin):
    list_display = ("cve", "severidade", "status", "scan")
    search_fields = ("cve", "descricao")
    list_filter = ("severidade", "status", "scan__tipo", "scan__projeto")

