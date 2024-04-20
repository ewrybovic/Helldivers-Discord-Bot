from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HomeWorld")


@_attrs_define
class HomeWorld:
    """Represents information about the homeworld(s) of a given race.

    Attributes:
        race (Union[Unset, int]): The identifier of the race (faction) this describes the homeworld of.
        planet_indices (Union[Unset, List[int]]): A list of Index identifiers.
    """

    race: Union[Unset, int] = UNSET
    planet_indices: Union[Unset, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        race = self.race

        planet_indices: Union[Unset, List[int]] = UNSET
        if not isinstance(self.planet_indices, Unset):
            planet_indices = self.planet_indices

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if race is not UNSET:
            field_dict["race"] = race
        if planet_indices is not UNSET:
            field_dict["planetIndices"] = planet_indices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        race = d.pop("race", UNSET)

        planet_indices = cast(List[int], d.pop("planetIndices", UNSET))

        home_world = cls(
            race=race,
            planet_indices=planet_indices,
        )

        return home_world
