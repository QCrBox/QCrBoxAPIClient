from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_interactive_session_parameters import CreateInteractiveSessionParameters
from ...models.q_cr_box_error_response import QCrBoxErrorResponse
from ...models.q_cr_box_response_interactive_session_id_response import QCrBoxResponseInteractiveSessionIDResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateInteractiveSessionParameters,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/interactive-sessions",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[QCrBoxErrorResponse, QCrBoxResponseInteractiveSessionIDResponse]]:
    if response.status_code == 201:
        response_201 = QCrBoxResponseInteractiveSessionIDResponse.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = QCrBoxErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = QCrBoxErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = QCrBoxErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[QCrBoxErrorResponse, QCrBoxResponseInteractiveSessionIDResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateInteractiveSessionParameters,
) -> Response[Union[QCrBoxErrorResponse, QCrBoxResponseInteractiveSessionIDResponse]]:
    """Create interactive session

     Create an interactive session with the provided arguments arguments.

    Args:
        body (CreateInteractiveSessionParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[QCrBoxErrorResponse, QCrBoxResponseInteractiveSessionIDResponse]]
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
    body: CreateInteractiveSessionParameters,
) -> Optional[Union[QCrBoxErrorResponse, QCrBoxResponseInteractiveSessionIDResponse]]:
    """Create interactive session

     Create an interactive session with the provided arguments arguments.

    Args:
        body (CreateInteractiveSessionParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[QCrBoxErrorResponse, QCrBoxResponseInteractiveSessionIDResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateInteractiveSessionParameters,
) -> Response[Union[QCrBoxErrorResponse, QCrBoxResponseInteractiveSessionIDResponse]]:
    """Create interactive session

     Create an interactive session with the provided arguments arguments.

    Args:
        body (CreateInteractiveSessionParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[QCrBoxErrorResponse, QCrBoxResponseInteractiveSessionIDResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateInteractiveSessionParameters,
) -> Optional[Union[QCrBoxErrorResponse, QCrBoxResponseInteractiveSessionIDResponse]]:
    """Create interactive session

     Create an interactive session with the provided arguments arguments.

    Args:
        body (CreateInteractiveSessionParameters):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[QCrBoxErrorResponse, QCrBoxResponseInteractiveSessionIDResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
