from qcrboxapiclient.client import Client
from qcrboxapiclient.models.create_data_file_the_file_to_upload import CreateDataFileTheFileToUpload
from qcrboxapiclient.models.q_cr_box_error_response import QCrBoxErrorResponse
from qcrboxapiclient.models.q_cr_box_response_data_files_response import QCrBoxResponseDataFilesResponse


def list_data_files(client: Client) -> QCrBoxResponseDataFilesResponse | QCrBoxErrorResponse:
    from qcrboxapiclient.api.data_files import list_data_files

    return list_data_files.sync(client=client)


def create_data_file(
    client: Client, body: CreateDataFileTheFileToUpload
) -> QCrBoxResponseDataFilesResponse | QCrBoxErrorResponse:
    from qcrboxapiclient.api.data_files import create_data_file

    return create_data_file.sync(body=body, client=client)
