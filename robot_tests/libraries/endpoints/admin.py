from qcrboxapiclient.client import Client
from qcrboxapiclient.models import QCrBoxErrorResponse, QCrBoxHealthResponse


def heatlhz(client: Client) -> QCrBoxHealthResponse | QCrBoxErrorResponse:
    from qcrboxapiclient.api.admin import healthz

    return healthz.sync(client=client)
