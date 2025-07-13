# core/gateway/veracode_gateway.py

import requests
from django.conf import settings


class VeracodeGateway:
    def __init__(self):
        self.base_url = settings.VERACODE_API_BASE_URL
        self.api_key = settings.VERACODE_API_KEY

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    # 🔍 WORKSPACES
    def list_workspaces(self):
        url = f"{self.base_url}/srcclr/v3/workspaces"
        return requests.get(url, headers=self._headers()).json()

    def get_workspace(self, workspace_id):
        url = f"{self.base_url}/srcclr/v3/workspaces/{workspace_id}"
        return requests.get(url, headers=self._headers()).json()

    def get_project(self, workspace_id, project_id):
        url = f"{self.base_url}/srcclr/v3/workspaces/{workspace_id}/projects/{project_id}"
        return requests.get(url, headers=self._headers()).json()

    def list_project_issues(self, workspace_id, project_id):
        url = f"{self.base_url}/srcclr/v3/workspaces/{workspace_id}/projects/{project_id}/issues"
        return requests.get(url, headers=self._headers()).json()

    def list_sca_scans(self, workspace_id):
        url = f"{self.base_url}/srcclr/v3/workspaces/{workspace_id}/scans"
        return requests.get(url, headers=self._headers()).json()

    def get_scan_details(self, scan_id):
        url = f"{self.base_url}/srcclr/v3/scans/{scan_id}"
        return requests.get(url, headers=self._headers()).json()

    def get_sca_findings(self, scan_id):
        url = f"{self.base_url}/srcclr/v3/scans/{scan_id}/findings"
        return requests.get(url, headers=self._headers()).json()

    def get_issue_details(self, issue_id):
        url = f"{self.base_url}/srcclr/v3/issues/{issue_id}"
        return requests.get(url, headers=self._headers()).json()