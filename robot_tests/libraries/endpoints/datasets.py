from qcrboxapiclient.client import Client
from qcrboxapiclient.models.create_dataset_body import CreateDatasetBody
from qcrboxapiclient.models.q_cr_box_error_response import QCrBoxErrorResponse
from qcrboxapiclient.models.q_cr_box_response_datasets_response import QCrBoxResponseDatasetsResponse


def list_datasets(client: Client) -> QCrBoxResponseDatasetsResponse | QCrBoxErrorResponse:
    from qcrboxapiclient.api.datasets import list_datasets

    return list_datasets.sync(client=client)


def create_dataset(client: Client, body: CreateDatasetBody) -> QCrBoxResponseDatasetsResponse | QCrBoxErrorResponse:
    from qcrboxapiclient.api.datasets import create_dataset

    return create_dataset.sync(body=body, client=client)


def delete_dataset_by_id(client: Client, id: str) -> None:
    from qcrboxapiclient.api.datasets import delete_dataset_by_id

    return delete_dataset_by_id.sync(id=id, client=client)


def get_dataset_by_id(client: Client, id: str) -> QCrBoxResponseDatasetsResponse | QCrBoxErrorResponse:
    from qcrboxapiclient.api.datasets import get_dataset_by_id

    return get_dataset_by_id.sync(id=id, client=client)

def download_dataset_by_id(client: Client, id: str) -> bytes | str | QCrBoxErrorResponse:
    from qcrboxapiclient.api.datasets import download_dataset_by_id

    return download_dataset_by_id.sync(id=id, client=client)