from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Position")


@_attrs_define
class Position:
    """Represents a position on the galactic war map.

    Attributes:
        x (Union[Unset, float]): The X coordinate.
        y (Union[Unset, float]): The Y coordinate.
    """

    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        x = self.x

        y = self.y

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        position = cls(
            x=x,
            y=y,
        )

        return position
