from qcrboxapiclient.client import Client
from qcrboxapiclient.models.q_cr_box_error_response import QCrBoxErrorResponse
from qcrboxapiclient.models.q_cr_box_response_applications_response import QCrBoxResponseApplicationsResponse


def list_applications(client: Client) -> QCrBoxResponseApplicationsResponse | QCrBoxErrorResponse | None:
    from qcrboxapiclient.api.applications import list_applications

    return list_applications.sync(client=client)
