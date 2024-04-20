from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Reward")


@_attrs_define
class Reward:
    """Represents the reward of an Assignment.

    Attributes:
        type (Union[Unset, int]): The type of reward, currently only one value is known: 1 which represents Medals
        id32 (Union[Unset, int]): Internal identifier of this Reward.
        amount (Union[Unset, int]): The amount of Type the players will receive upon completion.
    """

    type: Union[Unset, int] = UNSET
    id32: Union[Unset, int] = UNSET
    amount: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        id32 = self.id32

        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id32 is not UNSET:
            field_dict["id32"] = id32
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        id32 = d.pop("id32", UNSET)

        amount = d.pop("amount", UNSET)

        reward = cls(
            type=type,
            id32=id32,
            amount=amount,
        )

        return reward
