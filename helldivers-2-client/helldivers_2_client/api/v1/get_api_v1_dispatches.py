from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dispatch import Dispatch
from ...types import Response


def _get_kwargs(
    index: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/dispatches/{index}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Dispatch]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Dispatch.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Dispatch]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    index: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Dispatch]:
    """Fetches a specific Dispatch identified by index.

    Args:
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dispatch]
    """

    kwargs = _get_kwargs(
        index=index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    index: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Dispatch]:
    """Fetches a specific Dispatch identified by index.

    Args:
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dispatch
    """

    return sync_detailed(
        index=index,
        client=client,
    ).parsed


async def asyncio_detailed(
    index: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Dispatch]:
    """Fetches a specific Dispatch identified by index.

    Args:
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dispatch]
    """

    kwargs = _get_kwargs(
        index=index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    index: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Dispatch]:
    """Fetches a specific Dispatch identified by index.

    Args:
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dispatch
    """

    return (
        await asyncio_detailed(
            index=index,
            client=client,
        )
    ).parsed
