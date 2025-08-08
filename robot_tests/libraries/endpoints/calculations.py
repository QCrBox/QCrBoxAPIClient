from qcrboxapiclient.client import Client
from qcrboxapiclient.models.q_cr_box_error_response import QCrBoxErrorResponse
from qcrboxapiclient.models.q_cr_box_response_calculation_stopped_response import (
    QCrBoxResponseCalculationStoppedResponse,
)
from qcrboxapiclient.models.q_cr_box_response_calculations_response import QCrBoxResponseCalculationsResponse


def list_calculations(client: Client) -> QCrBoxResponseCalculationsResponse | QCrBoxErrorResponse | None:
    from qcrboxapiclient.api.calculations import list_calculations

    return list_calculations.sync(client=client)


def get_calculation_by_id(client: Client, id: str) -> QCrBoxResponseCalculationsResponse | QCrBoxErrorResponse | None:
    from qcrboxapiclient.api.calculations import get_calculation_by_id

    return get_calculation_by_id.sync(id=id, client=client)


def stop_running_calculation(
    client: Client, id: str
) -> QCrBoxResponseCalculationStoppedResponse | QCrBoxErrorResponse | None:
    from qcrboxapiclient.api.calculations import stop_running_calculation

    return stop_running_calculation.sync(id=id, client=client)
