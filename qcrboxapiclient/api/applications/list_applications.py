from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.q_cr_box_error_response import QCrBoxErrorResponse
from ...models.q_cr_box_response_applications_response import QCrBoxResponseApplicationsResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/applications",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[QCrBoxErrorResponse, QCrBoxResponseApplicationsResponse]]:
    if response.status_code == 200:
        response_200 = QCrBoxResponseApplicationsResponse.from_dict(response.json())

        return response_200
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
) -> Response[Union[QCrBoxErrorResponse, QCrBoxResponseApplicationsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[QCrBoxErrorResponse, QCrBoxResponseApplicationsResponse]]:
    """List all applications

     Retrieve a list of registered applications.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[QCrBoxErrorResponse, QCrBoxResponseApplicationsResponse]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[QCrBoxErrorResponse, QCrBoxResponseApplicationsResponse]]:
    """List all applications

     Retrieve a list of registered applications.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[QCrBoxErrorResponse, QCrBoxResponseApplicationsResponse]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[QCrBoxErrorResponse, QCrBoxResponseApplicationsResponse]]:
    """List all applications

     Retrieve a list of registered applications.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[QCrBoxErrorResponse, QCrBoxResponseApplicationsResponse]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[QCrBoxErrorResponse, QCrBoxResponseApplicationsResponse]]:
    """List all applications

     Retrieve a list of registered applications.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[QCrBoxErrorResponse, QCrBoxResponseApplicationsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
