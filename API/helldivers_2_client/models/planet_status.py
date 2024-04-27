from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanetStatus")


@_attrs_define
class PlanetStatus:
    """Represents the 'current' status of a planet in the galactic war.

    Attributes:
        index (Union[Unset, int]): The identifier of the PlanetInfo this status refers to.
        owner (Union[Unset, int]): The faction currently owning the planet.
        health (Union[Unset, int]): The current health / liberation of a planet.
        regen_per_second (Union[Unset, float]): If left alone, how much the health of the planet would regenerate.
        players (Union[Unset, int]): The amount of helldivers currently active on this planet.
    """

    index: Union[Unset, int] = UNSET
    owner: Union[Unset, int] = UNSET
    health: Union[Unset, int] = UNSET
    regen_per_second: Union[Unset, float] = UNSET
    players: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        index = self.index

        owner = self.owner

        health = self.health

        regen_per_second = self.regen_per_second

        players = self.players

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if owner is not UNSET:
            field_dict["owner"] = owner
        if health is not UNSET:
            field_dict["health"] = health
        if regen_per_second is not UNSET:
            field_dict["regenPerSecond"] = regen_per_second
        if players is not UNSET:
            field_dict["players"] = players

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        index = d.pop("index", UNSET)

        owner = d.pop("owner", UNSET)

        health = d.pop("health", UNSET)

        regen_per_second = d.pop("regenPerSecond", UNSET)

        players = d.pop("players", UNSET)

        planet_status = cls(
            index=index,
            owner=owner,
            health=health,
            regen_per_second=regen_per_second,
            players=players,
        )

        return planet_status
