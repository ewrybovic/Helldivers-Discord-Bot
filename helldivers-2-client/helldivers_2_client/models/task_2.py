from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Task2")


@_attrs_define
class Task2:
    """Represents a task in an Assignment that needs to be completed
    to finish the assignment.

        Attributes:
            type (Union[Unset, int]): The type of task this represents.
            values (Union[Unset, List[int]]): A list of numbers, purpose unknown.
            value_types (Union[Unset, List[int]]): A list of numbers, purpose unknown
    """

    type: Union[Unset, int] = UNSET
    values: Union[Unset, List[int]] = UNSET
    value_types: Union[Unset, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        values: Union[Unset, List[int]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        value_types: Union[Unset, List[int]] = UNSET
        if not isinstance(self.value_types, Unset):
            value_types = self.value_types

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if values is not UNSET:
            field_dict["values"] = values
        if value_types is not UNSET:
            field_dict["valueTypes"] = value_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        values = cast(List[int], d.pop("values", UNSET))

        value_types = cast(List[int], d.pop("valueTypes", UNSET))

        task_2 = cls(
            type=type,
            values=values,
            value_types=value_types,
        )

        return task_2
