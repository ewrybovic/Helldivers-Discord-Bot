import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dispatch")


@_attrs_define
class Dispatch:
    """A message from high command to the players, usually updates on the status of the war effort.

    Attributes:
        id (Union[Unset, int]): The unique identifier of this dispatch.
        published (Union[Unset, datetime.datetime]): When the dispatch was published.
        type (Union[Unset, int]): The type of dispatch, purpose unknown.
        message (Union[Unset, str]): The message this dispatch represents.
    """

    id: Union[Unset, int] = UNSET
    published: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        published: Union[Unset, str] = UNSET
        if not isinstance(self.published, Unset):
            published = self.published.isoformat()

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

        _published = d.pop("published", UNSET)
        published: Union[Unset, datetime.datetime]
        if isinstance(_published, Unset):
            published = UNSET
        else:
            published = isoparse(_published)

        type = d.pop("type", UNSET)

        message = d.pop("message", UNSET)

        dispatch = cls(
            id=id,
            published=published,
            type=type,
            message=message,
        )

        return dispatch
