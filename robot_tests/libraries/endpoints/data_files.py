from qcrboxapiclient.client import Client
from qcrboxapiclient.models.q_cr_box_error_response import QCrBoxErrorResponse
from qcrboxapiclient.models.q_cr_box_response_data_files_response import QCrBoxResponseDataFilesResponse


def list_data_files(client: Client) -> QCrBoxResponseDataFilesResponse | QCrBoxErrorResponse | None:
    from qcrboxapiclient.api.data_files import list_data_files

    return list_data_files.sync(client=client)


def get_data_file_by_id(client: Client, id: str) -> QCrBoxResponseDataFilesResponse | QCrBoxErrorResponse | None:
    from qcrboxapiclient.api.data_files import get_data_file_by_id

    return get_data_file_by_id.sync(id=id, client=client)


def download_data_file_by_id(client: Client, id: str) -> bytes | str | QCrBoxErrorResponse | None:
    from qcrboxapiclient.api.data_files import download_data_file_by_id

    return download_data_file_by_id.sync(id=id, client=client)
