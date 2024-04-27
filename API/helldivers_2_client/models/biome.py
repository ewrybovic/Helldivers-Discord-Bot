from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Biome")


@_attrs_define
class Biome:
    """Represents information about a biome of a planet.

    Attributes:
        name (Union[Unset, str]): The name of this biome.
        description (Union[Unset, str]): A human-readable description of the biome.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        biome = cls(
            name=name,
            description=description,
        )

        return biome
