from qcrboxapiclient.client import Client
from qcrboxapiclient.models.applications_response import ApplicationsResponse
from qcrboxapiclient.models.q_cr_box_error_response import QCrBoxErrorResponse


def list_applications(client: Client) -> ApplicationsResponse | QCrBoxErrorResponse:
    """List registered applications.

    Parameters
    ----------
    client : Client
        A QCrBoxAPIClient client.

    Returns
    -------
    Response
        A success or error response.
    """
    from qcrboxapiclient.api.applications import list_applications

    return list_applications.sync(client=client)
