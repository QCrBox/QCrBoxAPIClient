from qcrboxapiclient.client import Client
from qcrboxapiclient.models.invoke_command_parameters import InvokeCommandParameters
from qcrboxapiclient.models.q_cr_box_error_response import QCrBoxErrorResponse
from qcrboxapiclient.models.q_cr_box_response_commands_response import QCrBoxResponseCommandsResponse
from qcrboxapiclient.models.q_cr_box_response_invoke_command_response import QCrBoxResponseInvokeCommandResponse


def list_commands(client: Client) -> QCrBoxResponseCommandsResponse | QCrBoxErrorResponse | None:
    from qcrboxapiclient.api.commands import list_commands

    return list_commands.sync(client=client)


def get_command_by_id(client: Client, id: int) -> QCrBoxResponseCommandsResponse | QCrBoxErrorResponse | None:
    from qcrboxapiclient.api.commands import get_command_by_id

    return get_command_by_id.sync(id=id, client=client)


def invoke_command(
    client: Client, body: InvokeCommandParameters
) -> QCrBoxResponseInvokeCommandResponse | QCrBoxErrorResponse | None:
    from qcrboxapiclient.api.commands import invoke_command

    return invoke_command.sync(client=client, body=body)
