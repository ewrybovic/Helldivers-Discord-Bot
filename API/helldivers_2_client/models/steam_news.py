import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SteamNews")


@_attrs_define
class SteamNews:
    """Represents a new article from Steam's news feed.

    Attributes:
        id (Union[Unset, str]): The identifier assigned by Steam to this news item.
        title (Union[Unset, str]): The title of the Steam news item.
        url (Union[Unset, str]): The URL to Steam where this news item was posted.
        author (Union[Unset, str]): The author who posted this message on Steam.
        content (Union[Unset, str]): The message posted by Steam, currently in Steam's weird markdown format.
        published_at (Union[Unset, datetime.datetime]): When this message was posted.
    """

    id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    author: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    published_at: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        title = self.title

        url = self.url

        author = self.author

        content = self.content

        published_at: Union[Unset, str] = UNSET
        if not isinstance(self.published_at, Unset):
            published_at = self.published_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if author is not UNSET:
            field_dict["author"] = author
        if content is not UNSET:
            field_dict["content"] = content
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        author = d.pop("author", UNSET)

        content = d.pop("content", UNSET)

        _published_at = d.pop("publishedAt", UNSET)
        published_at: Union[Unset, datetime.datetime]
        if isinstance(_published_at, Unset):
            published_at = UNSET
        else:
            published_at = isoparse(_published_at)

        steam_news = cls(
            id=id,
            title=title,
            url=url,
            author=author,
            content=content,
            published_at=published_at,
        )

        return steam_news
