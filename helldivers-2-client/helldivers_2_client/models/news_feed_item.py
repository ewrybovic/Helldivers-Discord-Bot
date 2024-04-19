from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewsFeedItem")


@_attrs_define
class NewsFeedItem:
    """Represents an item in the newsfeed of Super Earth.

    Attributes:
        id (Union[Unset, int]): The identifier of this newsfeed item.
        published (Union[Unset, int]): A unix timestamp (in seconds) when this item was published.
        type (Union[Unset, int]): A numerical type, purpose unknown.
        message (Union[Unset, str]): The message containing a human readable text.
    """

    id: Union[Unset, int] = UNSET
    published: Union[Unset, int] = UNSET
    type: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        published = self.published

        type = self.type

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if published is not UNSET:
            field_dict["published"] = published
        if type is not UNSET:
            field_dict["type"] = type
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        published = d.pop("published", UNSET)

        type = d.pop("type", UNSET)

        message = d.pop("message", UNSET)

        news_feed_item = cls(
            id=id,
            published=published,
            type=type,
            message=message,
        )

        return news_feed_item
