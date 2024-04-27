from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.planet import Planet


T = TypeVar("T", bound="Campaign2")


@_attrs_define
class Campaign2:
    """Represents an ongoing campaign on a planet.

    Attributes:
        id (Union[Unset, int]): The unique identifier of this Campaign.
        planet (Union[Unset, Planet]): Contains all aggregated information AH has about a planet.
        type (Union[Unset, int]): The type of campaign, this should be mapped onto an enum.
        count (Union[Unset, int]): Indicates how many campaigns have already been fought on this Planet.
    """

    id: Union[Unset, int] = UNSET
    planet: Union[Unset, "Planet"] = UNSET
    type: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        planet: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.planet, Unset):
            planet = self.planet.to_dict()

        type = self.type

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if planet is not UNSET:
            field_dict["planet"] = planet
        if type is not UNSET:
            field_dict["type"] = type
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.planet import Planet

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _planet = d.pop("planet", UNSET)
        planet: Union[Unset, Planet]
        if isinstance(_planet, Unset):
            planet = UNSET
        else:
            planet = Planet.from_dict(_planet)

        type = d.pop("type", UNSET)

        count = d.pop("count", UNSET)

        campaign_2 = cls(
            id=id,
            planet=planet,
            type=type,
            count=count,
        )

        return campaign_2
