from qcrboxapiclient.client import Client
from qcrboxapiclient.models.q_cr_box_error_response import QCrBoxErrorResponse
from qcrboxapiclient.models.q_cr_box_response_commands_response import QCrBoxResponseCommandsResponse


def list_commands(client: Client) -> QCrBoxResponseCommandsResponse | QCrBoxErrorResponse:
    from qcrboxapiclient.api.commands import list_commands

    return list_commands.sync(client=client)


def get_command_by_id(client: Client) -> QCrBoxResponseCommandsResponse | QCrBoxErrorResponse:
    from qcrboxapiclient.api.commands import get_command_by_id

    return get_command_by_id.sync(client=client)
