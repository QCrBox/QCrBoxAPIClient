from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_data_file_the_file_to_upload import CreateDataFileTheFileToUpload
from ...models.q_cr_box_response_data_files_response import QCrBoxResponseDataFilesResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateDataFileTheFileToUpload,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/data-files",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[QCrBoxResponseDataFilesResponse]:
    if response.status_code == 201:
        response_201 = QCrBoxResponseDataFilesResponse.from_dict(response.text)

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[QCrBoxResponseDataFilesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateDataFileTheFileToUpload,
) -> Response[QCrBoxResponseDataFilesResponse]:
    """Upload a data file

     Upload a new data file to the data store.

    Args:
        body (CreateDataFileTheFileToUpload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QCrBoxResponseDataFilesResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateDataFileTheFileToUpload,
) -> Optional[QCrBoxResponseDataFilesResponse]:
    """Upload a data file

     Upload a new data file to the data store.

    Args:
        body (CreateDataFileTheFileToUpload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QCrBoxResponseDataFilesResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateDataFileTheFileToUpload,
) -> Response[QCrBoxResponseDataFilesResponse]:
    """Upload a data file

     Upload a new data file to the data store.

    Args:
        body (CreateDataFileTheFileToUpload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QCrBoxResponseDataFilesResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateDataFileTheFileToUpload,
) -> Optional[QCrBoxResponseDataFilesResponse]:
    """Upload a data file

     Upload a new data file to the data store.

    Args:
        body (CreateDataFileTheFileToUpload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QCrBoxResponseDataFilesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
