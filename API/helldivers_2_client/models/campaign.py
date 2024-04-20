from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Campaign")


@_attrs_define
class Campaign:
    """Contains information of ongoing campaigns.

    Attributes:
        id (Union[Unset, int]): The identifier of this campaign.
        planet_index (Union[Unset, int]): The Index of the planet this campaign refers to.
        type (Union[Unset, int]): A numerical type, indicates the type of campaign (see helldivers-2/json).
        count (Union[Unset, int]): A numerical count, the amount of campaigns the planet has seen.
    """

    id: Union[Unset, int] = UNSET
    planet_index: Union[Unset, int] = UNSET
    type: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        planet_index = self.planet_index

        type = self.type

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if planet_index is not UNSET:
            field_dict["planetIndex"] = planet_index
        if type is not UNSET:
            field_dict["type"] = type
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        planet_index = d.pop("planetIndex", UNSET)

        type = d.pop("type", UNSET)

        count = d.pop("count", UNSET)

        campaign = cls(
            id=id,
            planet_index=planet_index,
            type=type,
            count=count,
        )

        return campaign
