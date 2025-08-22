from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_data_file_body import CreateDataFileBody
from ...models.q_cr_box_error_response import QCrBoxErrorResponse
from ...models.q_cr_box_response_data_files_response import QCrBoxResponseDataFilesResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateDataFileBody,
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
) -> Optional[Union[QCrBoxErrorResponse, QCrBoxResponseDataFilesResponse]]:
    if response.status_code == 201:
        response_201 = QCrBoxResponseDataFilesResponse.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = QCrBoxErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = QCrBoxErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[QCrBoxErrorResponse, QCrBoxResponseDataFilesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateDataFileBody,
) -> Response[Union[QCrBoxErrorResponse, QCrBoxResponseDataFilesResponse]]:
    """Create a new data file

     Create a new dataset by uploading data files.

    Args:
        body (CreateDataFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[QCrBoxErrorResponse, QCrBoxResponseDataFilesResponse]]
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
    body: CreateDataFileBody,
) -> Optional[Union[QCrBoxErrorResponse, QCrBoxResponseDataFilesResponse]]:
    """Create a new data file

     Create a new dataset by uploading data files.

    Args:
        body (CreateDataFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[QCrBoxErrorResponse, QCrBoxResponseDataFilesResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateDataFileBody,
) -> Response[Union[QCrBoxErrorResponse, QCrBoxResponseDataFilesResponse]]:
    """Create a new data file

     Create a new dataset by uploading data files.

    Args:
        body (CreateDataFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[QCrBoxErrorResponse, QCrBoxResponseDataFilesResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateDataFileBody,
) -> Optional[Union[QCrBoxErrorResponse, QCrBoxResponseDataFilesResponse]]:
    """Create a new data file

     Create a new dataset by uploading data files.

    Args:
        body (CreateDataFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[QCrBoxErrorResponse, QCrBoxResponseDataFilesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
