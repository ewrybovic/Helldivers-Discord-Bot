from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.steam_news import SteamNews
from ...types import Response


def _get_kwargs(
    gid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/steam/{gid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["SteamNews"]]]:
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SteamNews.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, List["SteamNews"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, List["SteamNews"]]]:
    """Fetches a specific newsfeed item from the Helldivers 2 Steam newsfeed.

     You can definitely get this yourself, however it's included for your convenience!

    Args:
        gid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['SteamNews']]]
    """

    kwargs = _get_kwargs(
        gid=gid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, List["SteamNews"]]]:
    """Fetches a specific newsfeed item from the Helldivers 2 Steam newsfeed.

     You can definitely get this yourself, however it's included for your convenience!

    Args:
        gid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['SteamNews']]
    """

    return sync_detailed(
        gid=gid,
        client=client,
    ).parsed


async def asyncio_detailed(
    gid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, List["SteamNews"]]]:
    """Fetches a specific newsfeed item from the Helldivers 2 Steam newsfeed.

     You can definitely get this yourself, however it's included for your convenience!

    Args:
        gid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['SteamNews']]]
    """

    kwargs = _get_kwargs(
        gid=gid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, List["SteamNews"]]]:
    """Fetches a specific newsfeed item from the Helldivers 2 Steam newsfeed.

     You can definitely get this yourself, however it's included for your convenience!

    Args:
        gid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['SteamNews']]
    """

    return (
        await asyncio_detailed(
            gid=gid,
            client=client,
        )
    ).parsed
