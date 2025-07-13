from django.http import JsonResponse
from ..services.scan_service import ScanService

scan_service = ScanService()


def sync_all_view(request):
    scan_service.sync_todos_os_workspaces()
    return JsonResponse({"status": "OK", "message": "Todos os workspaces sincronizados"})


def sync_workspace_view(request, workspace_id):
    scan_service.sync_workspace(workspace_id)
    return JsonResponse({"status": "OK", "message": f"Workspace {workspace_id} sincronizado"})


def sync_projeto_view(request, nome):
    scan_service.sync_projeto_por_nome(nome)
    return JsonResponse({"status": "OK", "message": f"Projeto {nome} sincronizado"})