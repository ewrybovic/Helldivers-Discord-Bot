from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Reward2")


@_attrs_define
class Reward2:
    """The reward for completing an Assignment.

    Attributes:
        type (Union[Unset, int]): The type of reward (medals, super credits, ...).
        amount (Union[Unset, int]): The amount of Type that will be awarded.
    """

    type: Union[Unset, int] = UNSET
    amount: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        amount = d.pop("amount", UNSET)

        reward_2 = cls(
            type=type,
            amount=amount,
        )

        return reward_2
