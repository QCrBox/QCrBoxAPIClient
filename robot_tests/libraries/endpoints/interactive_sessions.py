from qcrboxapiclient.client import Client
from qcrboxapiclient.models.create_interactive_session import CreateInteractiveSession
from qcrboxapiclient.models.q_cr_box_error_response import QCrBoxErrorResponse
from qcrboxapiclient.models.q_cr_box_response_interactive_session_id_response import (
    QCrBoxResponseInteractiveSessionIDResponse,
)
from qcrboxapiclient.models.q_cr_box_response_interactive_sessions_response import (
    QCrBoxResponseInteractiveSessionsResponse,
)


def close_interactive_session(client: Client, id: str) -> None | QCrBoxErrorResponse:
    from qcrboxapiclient.api.interactive_sessions import close_interactive_session

    return close_interactive_session.sync(id=id, client=client)


def create_interactive_session_with_arguments(
    client: Client, body: CreateInteractiveSession
) -> QCrBoxResponseInteractiveSessionIDResponse | QCrBoxErrorResponse:
    from qcrboxapiclient.api.interactive_sessions import create_interactive_session_with_arguments

    return create_interactive_session_with_arguments.sync(client=client, body=body)


def get_interactive_session_by_id(
    client: Client, id: str
) -> QCrBoxResponseInteractiveSessionsResponse | QCrBoxErrorResponse:
    from qcrboxapiclient.api.interactive_sessions import get_interactive_session_by_id

    return get_interactive_session_by_id.sync(id=id, client=client)


def list_interactive_sessions(client: Client) -> QCrBoxResponseInteractiveSessionsResponse | QCrBoxErrorResponse:
    from qcrboxapiclient.api.interactive_sessions import list_interactive_sessions

    return list_interactive_sessions.sync(client=client)
