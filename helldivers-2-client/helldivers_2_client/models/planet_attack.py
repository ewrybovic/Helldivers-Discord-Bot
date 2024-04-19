from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanetAttack")


@_attrs_define
class PlanetAttack:
    """Represents an attack on a PlanetInfo.

    Attributes:
        source (Union[Unset, int]): Where the attack originates from.
        target (Union[Unset, int]): The planet under attack.
    """

    source: Union[Unset, int] = UNSET
    target: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        source = self.source

        target = self.target

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source = d.pop("source", UNSET)

        target = d.pop("target", UNSET)

        planet_attack = cls(
            source=source,
            target=target,
        )

        return planet_attack
