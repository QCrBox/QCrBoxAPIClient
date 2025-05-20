from qcrboxapiclient.client import Client
from qcrboxapiclient.models.q_cr_box_error_response import QCrBoxErrorResponse
from qcrboxapiclient.models.q_cr_box_response_calculations_response import QCrBoxResponseCalculationsResponse


def list_calculations(client: Client) -> QCrBoxResponseCalculationsResponse | QCrBoxErrorResponse:
    from qcrboxapiclient.api.calculations import list_calculations

    return list_calculations.sync(client=client)


def get_calculation_by_id(client: Client) -> QCrBoxResponseCalculationsResponse | QCrBoxErrorResponse:
    from qcrboxapiclient.api.calculations import get_calculation_by_id

    return get_calculation_by_id.sync(client=client)
