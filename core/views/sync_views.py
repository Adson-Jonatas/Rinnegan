from django.http import JsonResponse
from core.services.scan_service import ScanService

scan = ScanService()


def sync_all(request):
    scan.sync_todos_os_workspaces()
    return JsonResponse({"status": "ok", "message": "Workspaces sincronizados!"})